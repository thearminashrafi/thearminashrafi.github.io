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

      // A single-line "$$...$$" with real content between the fences.
      // (A lone "$$" line -- the already-correct form -- has nothing
      // between the fences, so `(.+)` doesn't match it and it's left
      // untouched.)
      return part.replace(/^([ \t]*)\$\$(.+)\$\$[ \t]*$/gm, (_match, indent, content) => {
        return `${indent}$$\n${content}\n${indent}$$`
      })
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
