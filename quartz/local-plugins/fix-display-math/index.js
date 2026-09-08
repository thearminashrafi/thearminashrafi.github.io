// remark-math only treats $$...$$ as display (block) math when the
// opening and closing fences are each alone on their own line, like a
// fenced code block. Written inline as $$eq$$ on one line, it silently
// falls through to the *inline* math parser instead -- same content,
// but no centering and no proper display-style typesetting (e.g. sum/
// integral limits render compact instead of stacked).
//
// This transformer runs on the raw markdown text before any parsing,
// so it's the one place we can fix this for every note, permanently,
// without relying on remembering to format equations a particular way.

const FENCE_SPLIT = /(^```[\s\S]*?^```$)/m

function normalizeDisplayMath(src) {
  // Skip fenced code blocks so we never touch a literal "$$" inside a
  // code sample.
  const parts = src.split(FENCE_SPLIT)
  return parts
    .map((part, i) => {
      const isCodeFence = i % 2 === 1
      if (isCodeFence) return part

      let out = part

      // Case 1: a single-line "$$...$$" with real content between the
      // fences. (A lone "$$" line -- the already-correct form -- has
      // nothing between the fences, so `(.+)` doesn't match it and
      // it's left untouched.) Must run before cases 2/3 below, since
      // those look for a bare fence with content stuck to *one* side --
      // this is the case where content is stuck to *both* sides at
      // once and needs the full three-line split.
      out = out.replace(/^([ \t]*)\$\$(.+)\$\$[ \t]*$/gm, (_match, indent, content) => {
        return `${indent}$$\n${content}\n${indent}$$`
      })

      // Case 2: closing fence glued to the prose that follows it on
      // the same line, e.g. "...R_Y(Y))$$*Proof.* Let us start...".
      // Once case 1 has run, any "$$" that starts a line and still has
      // more content after it can only be this -- a well-formed lone
      // closing fence has nothing following. Split them onto separate
      // lines.
      out = out.replace(/^([ \t]*)\$\$([ \t]*\S[^\n]*)$/gm, (_match, indent, trailing) => {
        return `${indent}$$\n${trailing}`
      })

      // Case 3: opening fence glued to the prose that precedes it on
      // the same line, e.g. "as characterized by $$eq". Symmetric to
      // case 2 -- a well-formed lone opening fence has nothing before
      // it on its line.
      out = out.replace(/^([ \t]*\S[^\n]*[^\s$])\$\$[ \t]*$/gm, (_match, leading) => {
        return `${leading}\n$$`
      })

      return out
    })
    .join("")
}

export const FixDisplayMath = (_opts) => ({
  name: "FixDisplayMath",
  textTransform(_ctx, src) {
    return normalizeDisplayMath(src)
  },
})

export default FixDisplayMath
