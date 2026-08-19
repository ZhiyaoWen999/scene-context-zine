---
name: scene-context-zine
description: "Transform a user-supplied photo into a context-preserving editorial zine image by locking the scene's identity, background, palette, light, materials, density, and memory cues before choosing a Documentary Editorial, Multi-frame Joiner, Graphic Scene Poster, or Gathered Collage route. Use for photo-to-zine, editorial collage, travel-memory pages, scene posters, cutout or fragmented compositions, route previews, prompt planning, or when an earlier transformation lost the original place, white or brown background, lighting, atmosphere, or lived-in detail."
---

# 场景语境纸刊 · Scene Context Zine

Preserve the place before applying the graphic language. Treat the background as evidence, not leftover space.

**Original source:** *Gathered Scenes Zine v1.3* by Zeejay0, [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill), base commit `eae9a62e20cb570c0adabc94cb189b1c91b7be99`.

**Context-first reconstruction and maintenance:** zhiyaowen, 2026-08-18. Keep the original personal non-commercial license and attribution. This version is a modified derivative, not an official upstream release.

## Core Contract

Follow this equation:

```text
source photo
→ lock irreplaceable Scene Core
→ choose a composition route
→ set route strength and a visible transformation floor
→ map source information into every designed field
→ choose field, palette, abstraction, material, and memory modules
→ generate and compare against the lock
```

Resolve conflicts in this order:

1. Preserve scene identity and context-bearing background.
2. Preserve spatial relationships, native color atmosphere, and light.
3. Preserve meaningful complexity and lived-in evidence.
4. Preserve truthful source photography wherever the selected route uses photography.
5. Apply a route-specific transformation.
6. Add paper, print, typography, and decorative effects only when they support the scene.

Never let a default cream field, saturated accent, large blank area, fixed poster ratio, or generic poetic mood override the source. If the style and the memory disagree, keep the memory.

## Load Supporting References

- Read [scene-core.md](references/scene-core.md) before compiling any generation prompt; use its Scene Contract and module rules.
- Read [style-routes.md](references/style-routes.md) before choosing or comparing routes.
- Read [prompt-and-qa.md](references/prompt-and-qa.md) before image generation or targeted regeneration.
- Read [scene-examples.md](references/scene-examples.md) when calibrating interiors, white environments, night scenes, travel scenes, or dense lived-in rooms.
- Read [research-lineage.md](references/research-lineage.md) only when the user asks for historical research, influences, or new route development. Do not place artist or publication names in the final image prompt.
- Run `scripts/lint_scene_plan.py` when creating, debugging, or auditing a serialized JSON Scene Plan. It is optional during direct visual generation.

## Respect the Source and Privacy

- Treat a supplied photo plus a request to transform or generate as consent to use image generation; do not ask again.
- Visually inspect the source before editing. For a local image, use the available local-image viewer first.
- Use the supplied photo as an actual image-editing reference. Do not recreate it from text alone.
- Send only the final prompt and required reference image to the image-generation service.
- Do not browse, upload elsewhere, commit, or retain a private source photo unless the user explicitly asks.
- Do not invent identity, place, date, weather, or personal facts.

## Choose the Operating Mode

- **Generate:** inspect, select one route, compile, generate, verify, and return the image. Proceed directly when the request is clear.
- **Route preview:** return two to four distinct route cards without generating. Include what each route preserves, transforms, and risks.
- **Prompt only:** return the Scene Contract, selected modules, and final generation prompt without calling image generation.
- **Explicit route:** honor the user's route unless it would destroy a stated Scene Lock; explain any necessary adjustment briefly.

## Step 1 — Build the Scene Contract

Record these fields internally before styling:

- **Identity anchors:** three to five people, objects, landmarks, or shapes that make this scene specific.
- **Spatial invariants:** relative position, scale, overlap, facing direction, horizon, path, gaze, or perspective that must survive.
- **Context-bearing regions:** background areas whose removal would make the scene feel like “anywhere.”
- **Environmental palette:** background base, mid-tone, dark anchor, light temperature, and meaningful accent.
- **Light and time:** source direction, softness, contrast, interior/exterior mix, and visible time or weather cues.
- **Material signatures:** wood, plaster, tile, steel, glass, fabric, snow, water, foliage, paper, or other place-defining surfaces.
- **Density character:** sparse, orderly, layered, crowded, improvised, weathered, domestic, or monumental.
- **Memory cues:** a cup, sign, menu, reflection, ticket, date, shop name, gesture, or other detail that anchors the moment.
- **Semantic detail map:** classify detail as `preserve`, `compress`, `omit`, or `do_not_invent` according to meaning, not size.
- **Flexible zones:** list what may be cropped, simplified, repeated, recolored, or illustrated.

Ask: **If this region vanished, would the image still feel like this exact place and moment?** If no, lock it.

## Step 2 — Select One Primary Route

Use one route as the composition grammar. Add at most one secondary technique.

| Route | Balanced-strength photo share | Prefer when | Main transformation |
| --- | ---: | --- | --- |
| **Documentary Editorial** | 65–85% | context is fragile; interiors, cafés, white rooms, subtle light | quiet grid, crop, margins, small type |
| **Multi-frame Joiner** | 55–80% across source fragments | cutting is welcome; place detail, movement, multiple viewpoints | overlapping source crops, time/space fragmentation |
| **Graphic Scene Poster** | 45–65% | travel, architecture, landscape, signage, strong geometry | landmark anchor, scale shift, source-derived graphic planes |
| **Gathered Collage** | 30–50% | the user wants the original tactile torn-paper character | cutout, irregular tear, illustration continuation, selective print |

Every share in this table is the `balanced` default. Read the restrained and bold ranges from the route-strength table in [style-routes.md](references/style-routes.md); it is the single source of truth that `scripts/lint_scene_plan.py` enforces.

Default to **Documentary Editorial** when uncertain. It has the lowest context-loss risk. Do not choose Gathered Collage merely because the request contains the word “zine.”

## Step 2.5 — Set Route Strength and Transformation Floor

Treat **context fidelity as semantic and relational fidelity, not pixel fidelity**. Keeping the place does not require keeping the source as one continuous full-frame photograph.

Choose `restrained`, `balanced`, or `bold`; default to `balanced`. Use `restrained` only for fragile faces, subtle interiors, exact signage, or explicit low-change requests. Use `bold` when the user asks for clear differentiation and the Scene Lock is robust.

Before generation, define a visible transformation floor:

- Select at least one structural operation for `restrained`, two for `balanced`, and three for `bold`.
- Choose operations from: asymmetric content-derived grid, crop/scale shift, same-source fragment reassembly, source-derived graphic plane, boundary crossing, negative-space reallocation, directional cut, source-detail repetition, or subject cutout.
- For a balanced **Graphic Scene Poster**, reserve at least 25% of the canvas for visibly graphic, source-derived fields and keep 45–65% truthful photography. Increase the graphic field to at least 35% for `bold`.
- Require a source contour, fragment, or plane to cross one internal boundary in balanced/bold Graphic Scene Poster and Gathered Collage routes.
- Reject any result that remains a continuous full-frame photograph changed only by color grading, halftone, grain, saturation, or another surface treatment.

Use the **anchored synthesis** for landscape, architecture, and travel by default: keep one place-defining photographic anchor; organize it with an asymmetric grid derived from the source; add one source-derived plane; then choose either one same-source fragment or one directional cut. Keep halftone or overprint localized and optional.

## Step 2.75 — Build the Source-Information Translation Map

Do not treat the non-photographic area as decoration. For every paper field, graphic plane, illustrated continuation, connective gap, or repeated mark, record:

- **Source region:** the exact visible wall, sky, water, foliage, reflection, fabric, sign, contour, or object group being translated.
- **Translation mode:** `contour`, `silhouette`, `rhythm`, `same-source-crop`, `stencil`, `material-continuation`, `value-continuation`, `reflection-hatch`, `detail-repetition`, or `cut-paper`.
- **Continuity anchor:** the edge, axis, color/value relationship, overlap, direction, or material behavior that reconnects the translated field to the photograph.

At `balanced` or `bold`, every major designed field must carry at least one recognizable source cue. Calm breathing room may remain, but untranslated blank space must not dominate Graphic Scene Poster or Gathered Collage. Paper color, grain, halftone, or torn texture alone does not count as translated information.

Never replace source information with generic arrows, circles, botanical ornaments, diagram marks, decorative geometry, or invented symbols. A mark is allowed only when its shape, direction, rhythm, or semantic owner is visibly traceable to the source.

## Step 3 — Resolve Independent Modules

### Field tone

Choose one visible field treatment from the source:

- `source-tone` — derive the field from the dominant background; default.
- `material-continuation` — continue wall, sky, wood, water, snow, or ground.
- `neutral-paper` — use off-white, gray-white, or cream only when the source or route supports it.
- `dark-stock` — use charcoal, black, or deep brown for night or low-key scenes.
- `chromatic-stock` — enlarge a color already present in the source.
- `raw-photo` — use no paper field; build the design over or around the photograph.

Cream paper is one option, not a signature requirement.

### Palette

Choose one:

- `native` — introduce no new hue; default.
- `source-amplification` — enlarge or repeat a meaningful source color.
- `tonal-translation` — translate the source into adjacent pigments without changing its color relationship.
- `graphic-counterpoint` — introduce one contrasting print hue only when it has a clear compositional job.

If removing the accent changes nothing important, remove it. Do not add color merely to signal design.

### Abstraction

Use `light` abstraction by default. Increase only when the Scene Contract remains legible.

- Preserve meaningful complexity: signs, room objects, menu, window light, surface wear, landmark contours, and lived-in traces may be small yet essential.
- Compress redundant complexity: repeated chairs, leaves, windows, gravel, crowds, or texture may become rhythms or masses.
- Omit meaningless noise: artifacts, accidental clutter without scene value, and duplicated contours.
- Never “clean up” a lived-in environment into a generic minimalist room.

### Material and print

Choose zero or one primary print treatment: raw photographic, matte paper, source-colored paper, newsprint, selective RISO-like layer, photocopy, or cut paper. Localize grain, halftone, misregistration, dry ink, or fibers; do not filter the whole world unless explicitly requested.

### Typography and memory layer

Make text optional. Prefer no text over invented metadata.

- Reproduce user-supplied wording exactly.
- Allow real place, date, time, weather, ticket, menu, or map cues when supplied or visibly present.
- If authoring text, use one short source-grounded phrase; do not invent a quotation, address, or factual record.
- Keep type subordinate unless the user explicitly wants a poster headline.
- Use one typography system and maintain correct spelling.

## Step 4 — Compile the Generation Prompt

Write eight compact blocks:

1. **Reference and route:** state that the attached source photo is authoritative; name the formal route without artist names.
2. **Scene Lock:** state every identity anchor, spatial invariant, context-bearing region, palette role, light cue, material signature, density trait, and memory cue that must remain.
3. **Allocation and operations:** specify route strength, photographic presence, graphic-field share, structural operations, crop/fragments, hierarchy, eye path, flexible zones, and boundary crossing.
4. **Information translation:** map every major non-photo field to its source region, translation mode, and continuity anchor; state the untranslated blank-space limit.
5. **Field, palette, and abstraction:** specify modes, source derivation, preserve/compress/omit decisions, and exact introduced-hue limit.
6. **Material and text:** specify localized print behavior, edge treatment, exact wording, placement, hierarchy, or explicit absence of text.
7. **Capture integrity:** hold neutral white balance and the source light temperature, keep low-interest regions, tie grain to exposure, match one real lens, and keep material irregular at every scale.
8. **Hard constraints:** prohibit invented scenery, generic background replacement, global filters, unrelated motifs, damaged faces, illegible text, mockups, watermarks, and unintended 3D depth.

Use only instructions that can become visible pixels. Describe formal properties instead of naming artists, studios, publications, or copyrighted works.

The capture-integrity block exists because image models drift in predictable directions that attack this Skill's locks specifically: whites warm toward cream and shadows go muddy brown, every region gets raised to equal saturation, grain arrives as a uniform overlay, unmotivated rim light and haze appear, background blur ignores distance, and repeated material tiles instead of varying. Naming each drift is cheaper than repairing it after generation.

## Step 5 — Generate and Compare

1. Include the supplied photo as the editing reference.
2. Generate one image unless the user asks for variants.
3. Compare the result against every locked Scene Contract field at normal and thumbnail scale.
4. Apply the quality gate in [prompt-and-qa.md](references/prompt-and-qa.md).
5. Regenerate at most once with a targeted correction. Do not rewrite the entire style unless the selected route itself failed.

## Targeted Corrections

- **Generic place:** restore the missing context-bearing region and two material or memory cues.
- **Wrong white/brown field:** replace generic paper with the source background base or material continuation.
- **Atmosphere drift:** restore light temperature, contrast, weather/time cue, and native value range.
- **Generative rendering drift:** restore neutral white balance, source light temperature, low-interest regions, exposure-linked grain, single-lens focus falloff, and irregular material structure; remove unmotivated rim light, haze, or golden-hour cast.
- **Over-cleaned room:** restore semantic objects and the original density character.
- **Decorative color:** switch to native or source-amplification; remove detached accents.
- **Excessive blank space:** extend the context-bearing background or source-colored field.
- **Weak transformation:** keep the Scene Lock, then strengthen route-specific crop, scale, overlap, or hierarchy.
- **Texture-only result:** break the continuous full-frame photograph, restore the required graphic-field share, and execute the missing structural operations; keep all Scene Locks unchanged.
- **Empty or generic field:** restore information from the displaced source region using a named translation mode and reconnect it through a visible continuity anchor; remove invented arrows, circles, ornaments, or diagram marks.
- **Too many effects:** keep one primary material process and remove the rest.
- **Damaged person or landmark:** restore truthful source detail and reduce abstraction locally.
- **Text failure:** restore exact wording, spelling, hierarchy, and placement; remove invented metadata.

## Hard Avoids

Avoid generic cream replacement, fixed 3:5 output when another ratio fits, mandatory high-chroma accents, automatic 60–80% detail deletion, global RISO/Xerox filters, empty paper that erases place, generic arrows or diagram symbols, arbitrary geometric stickers, unrelated botanical ornaments, invented landmarks, beautified or sanitized lived-in rooms, fake metadata, multiple competing print processes, uniform tear frames, heavy drop shadows, curled paper, scrapbook depth, glossy mockups, cinematic depth of field, AI smoothing, illegible faces, misspelled text, logos, CTAs, and watermarks.

Keep cutouts, irregular crops, fragmentation, torn fibers, boundary crossing, source-shape continuation, hierarchy, paper tactility, and minor print imperfection available as techniques rather than mandatory signatures.

## Output

Return the generated image plus one compact Chinese rationale by default. State:

- which context cues were locked;
- which route was selected;
- what was transformed without replacing the place.

Return prompts, Scene Contracts, or detailed route notes only when requested.

Do not append promotional notices, website advertisements, or attribution boilerplate to ordinary generation replies. Keep license and source attribution in the repository documentation rather than repeating them in user-facing output.

## Final Quality Gate

Do not return the image unless all critical checks pass:

- Does it still feel like this exact place and moment, not merely the same subject?
- Are at least three identity anchors and all spatial invariants recognizable?
- Does at least one context-bearing background region survive?
- Do background base, light temperature, material signatures, and density character remain coherent with the source?
- Were meaningful details preserved and only redundant detail compressed?
- Is the chosen route visibly distinct and internally consistent?
- Does the result meet the selected route strength and transformation floor rather than relying on a surface filter?
- At thumbnail scale, is it visibly a designed editorial composition rather than the original photograph with texture?
- Can every major non-photographic field and graphic mark be traced to a named source region through a visible continuity anchor?
- Is untranslated blank space subordinate, with no generic symbol standing in for missing scene information?
- Were field tone, palette, abstraction, material, and text chosen independently from the source?
- Is any introduced hue source-justified and limited to one?
- Is the source photo used as a reference rather than reconstructed from prose?
- Are people, landmarks, typography, and factual metadata intact?

When a critical lock fails, regenerate once with the smallest correction that restores it.
