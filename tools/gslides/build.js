const pptxgen = require("pptxgenjs");
const fs = require("fs");
const spec = JSON.parse(fs.readFileSync("spec.json", "utf8"));
const bg = JSON.parse(fs.readFileSync("bg.json", "utf8"));
const md = fs.readFileSync(process.argv[2], "utf8");
// split slides.md into slides (skip frontmatter) and pull notes / DEMO comments
const parts = md.split(/\n---\n/).slice(1);
const notes = parts.map(p => {
  const demo = [...p.matchAll(/<!-- DEMO: ([\s\S]*?) -->/g)].map(m => "[DEMO] " + m[1].trim());
  const n = [...p.matchAll(/<!-- notes: ([\s\S]*?) -->/g)].map(m => m[1].trim());
  return [...demo, ...n].join("\n");
});
if (notes.length !== spec.slides.length) throw new Error(`notes ${notes.length} vs slides ${spec.slides.length}`);
const h = c => c.replace("#", "");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "[L1-01] 기억하는 여행 계획 만들기";
pres.theme = { headFontFace: "Noto Sans KR", bodyFontFace: "Noto Sans KR" };
spec.slides.forEach((s, i) => {
  const slide = pres.addSlide();
  slide.background = { color: h(bg[s.id]) };
  for (const el of s.elements) {
    const base = { x: el.x, y: el.y, w: el.w, objectName: el.id };
    const font = { fontFace: el.font || "Noto Sans KR", fontSize: el.size || 14, bold: !!el.bold, color: h(el.color || "#1F2937") };
    if (el.type === "table") {
      const border = [{ type: "none" }, { type: "none" }, { pt: 1, color: "E0E0E0" }, { type: "none" }];
      const rows = el.rows.map((r, ri) => r.map(c => ({ text: c, options: { ...font, bold: !!el.header && ri === 0, border, valign: "middle" } })));
      slide.addTable(rows, { ...base, colW: el.col_widths, rowH: el.row_h || 0.5, margin: [0.05, 0.1, 0.05, 0.1] });
    } else if (el.type === "text") {
      const align = (el.align || "START") === "CENTER" ? "center" : "left";
      let text = el.text;
      if (el.bullets) text = el.text.split("\n").map((t, k, a) => ({ text: t, options: { bullet: true, breakLine: k < a.length - 1, paraSpaceAfter: el.space_below || 8 } }));
      slide.addText(text, { ...base, h: el.h, ...font, align, valign: el.align === "CENTER" ? "middle" : "top", isTextBox: true, margin: 0.05 });
    } else {
      const align = (el.align || "START") === "CENTER" ? "center" : "left";
      slide.addText(el.text, { ...base, h: el.h, ...font, align, valign: "middle", shape: pres.ShapeType.roundRect, rectRadius: 0.12,
        fill: { color: h(el.fill || "#F3F4F6") }, line: { type: "none" }, margin: [0.15, 0.2, 0.15, 0.2] });
    }
  }
  slide.addNotes(notes[i]);
});
pres.writeFile({ fileName: "l1-01.pptx" }).then(f => console.log("wrote", f));
