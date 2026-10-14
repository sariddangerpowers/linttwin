// js_helper.mjs — parsing and ESLint helpers for linttwin's JavaScript checks (run with Node).
//   node js_helper.mjs <js_dir> classify <in.json> <out.json>  in: [{path, hint}]  out: [{path, sourceType|null, error}]
//   node js_helper.mjs <js_dir> oracle   <in.json> <out.json>  in: [{orig, fixed, sourceType}]  out: [{fixed, syntax, lost}]
//   node js_helper.mjs <js_dir> eslint   <in.json> <out.json>  in: {cwd, sourceType, files, rules, inline?}  out: [{path, msgs}]
//     inline: false ignores eslint-disable / eslint-env / global comments (for tools that do not read ESLint directives)
//     ESLint's Node API with no config lookup (overrideConfigFile: true), no ignore patterns, unused-directive reports off,
//     browser + node + es2021 globals; plugins: unicorn.
// sourceType: "module" or "commonjs" (espree, the parser ESLint itself uses). classify tries the hint first (Node's own
// rule: .mjs / package "type": "module" -> module, else commonjs), then the other type; null if neither parses.
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [jsDir, cmd, inFile, outFile] = process.argv.slice(2);
const require = createRequire(path.join(jsDir, "package.json"));
const espree = require("espree");

function parse(src, sourceType) {
  return espree.parse(src, { ecmaVersion: "latest", sourceType, comment: true, range: false, loc: false,
                              ecmaFeatures: { jsx: false, globalReturn: sourceType === "commonjs" } });
}

function tryParse(src, sourceType) {
  try { return [parse(src, sourceType), null]; } catch (e) { return [null, String(e.message || e)]; }
}

const items = JSON.parse(fs.readFileSync(inFile, "utf8"));
let out = [];
if (cmd === "classify") {
  for (const it of items) {
    let src;
    try { src = fs.readFileSync(it.path, "utf8"); } catch (e) { out.push({ path: it.path, sourceType: null, error: "read" }); continue; }
    if (src.startsWith("#!")) src = "//" + src.slice(2);          // ESLint strips a shebang the same way
    const order = it.hint === "module" ? ["module", "commonjs"] : ["commonjs", "module"];
    let st = null, err = null;
    for (const t of order) { const [ast, e] = tryParse(src, t); if (ast) { st = t; break; } err = err || e; }
    out.push({ path: it.path, sourceType: st, error: st ? null : err });
  }
} else if (cmd === "oracle") {
  const comments = (ast) => {
    const m = new Map();
    for (const c of ast.comments) { const k = c.type + ":" + c.value.trimEnd(); m.set(k, (m.get(k) || 0) + 1); }
    return m;
  };
  for (const it of items) {
    let a = fs.readFileSync(it.orig, "utf8"), b = fs.readFileSync(it.fixed, "utf8");
    if (a.startsWith("#!")) a = "//" + a.slice(2);
    if (b.startsWith("#!")) b = "//" + b.slice(2);
    const [ta] = tryParse(a, it.sourceType);
    const [tb, eb] = tryParse(b, it.sourceType);
    const r = { fixed: it.fixed, syntax: null, lost: [] };
    if (ta && !tb) r.syntax = eb;
    if (ta && tb) {
      const ca = comments(ta), cb = comments(tb);
      for (const [k, n] of ca) { const d = n - (cb.get(k) || 0); for (let i = 0; i < d && r.lost.length < 10; i++) r.lost.push(k.slice(0, 200)); }
    }
    out.push(r);
  }
}
else if (cmd === "eslint") {
  const { ESLint } = require("eslint");
  const globals = require("globals");
  const unicorn = (await import(pathToFileURL(require.resolve("eslint-plugin-unicorn")).href)).default;
  const eslint = new ESLint({
    cwd: items.cwd, overrideConfigFile: true, ignore: false, warnIgnored: false, allowInlineConfig: items.inline !== false,
    overrideConfig: [{
      files: ["**/*.js", "**/*.mjs", "**/*.cjs"],
      languageOptions: { ecmaVersion: "latest", sourceType: items.sourceType,
                         globals: { ...globals.browser, ...globals.node, ...globals.es2021 } },
      linterOptions: { reportUnusedDisableDirectives: "off" },
      plugins: { unicorn },
      rules: items.rules,
    }],
  });
  const res = await eslint.lintFiles(items.files);
  out = res.map((r) => ({ path: r.filePath, msgs: r.messages.map((m) => ({ rule: m.ruleId, line: m.line, col: m.column,
                                                                         msg: m.message, fatal: !!m.fatal })) }));
}
fs.writeFileSync(outFile, JSON.stringify(out));
