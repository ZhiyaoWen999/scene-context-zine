# Scene Core and Module Specification

## Contents

1. Scene Contract schema
2. Lock tests
3. Context-bearing background
4. Environmental palette
5. Semantic detail map
6. Field-tone modes
7. Palette modes
8. Abstraction levels
9. Material and typography modules
10. Transformation-floor fields
11. Source-information translation fields
12. JSON plan contract

## 1. Scene Contract schema

Complete this structure before route selection. Use visible evidence only.

```yaml
scene_core:
  identity_anchors:
    - three to five source-specific subjects or features
  spatial_invariants:
    - relative positions, scale, overlap, direction, horizon, or perspective
  context_bearing_regions:
    - region, why it identifies the place, minimum visible form
  environmental_palette:
    background_base: source color and material
    midtone: source color and role
    dark_anchor: source color and location
    light_temperature: warm/cool/neutral plus source relationship
    meaningful_accent: source color and semantic owner, or none
  light_time:
    - direction, softness, contrast, mixed light, weather, or time cue
  material_signatures:
    - two to five place-defining materials
  density_character: sparse | orderly | layered | crowded | improvised | weathered | monumental
  memory_cues:
    - source-grounded object, sign, reflection, gesture, or metadata
  detail_map:
    preserve:
      - small or large details whose meaning must survive
    compress:
      - repeated or redundant details that may become a mass or rhythm
    omit:
      - visually noisy details with no identity or memory role
    do_not_invent:
      - facts, objects, scenery, metadata, or identities absent from the source
  flexible_zones:
    - regions safe to crop, repeat, recolor, simplify, or illustrate
```

Write concrete observations. Prefer `warm walnut wall across upper-right half` over `warm background`; prefer `cold daylight rectangle at left window` over `nice lighting`.

## 2. Lock tests

Apply all four tests to any candidate anchor or region:

### Anywhere test

Remove the candidate mentally. If the scene becomes a generic café, room, beach, street, or landscape, lock it.

### Substitution test

Replace the candidate with a generic object or flat paper. If the memory changes materially, lock it.

### Relationship test

Check whether its meaning depends on another element: person-to-window, cup-to-table, tower-to-ridge, sign-to-storefront. Lock the relationship, not just both objects.

### Thumbnail test

Reduce the image mentally. Preserve the broad color/material region and directional relationship even when small detail cannot survive.

Classify a lock as **critical** when failure would change place, time, identity, or emotional fact. A critical lock overrides route aesthetics.

## 3. Context-bearing background

Treat background as a subject when it carries any of these:

- a distinctive wall, window, skyline, shoreline, mountain ridge, storefront, or room layout;
- mixed light that defines interior versus exterior;
- material contrast such as wood/white plaster, tile/steel, snow/dark water;
- visible use: stacked books, tools, clothes, menus, cables, plants, signs, or wear;
- scale evidence that explains where the person is;
- a culturally or geographically specific feature;
- a color field that dominates the memory of the scene.

Preserve at least one context-bearing region in every route. A region may remain photographic, become a set of source crops, or continue as a materially faithful graphic field. It may not become unrelated cream or empty paper.

### Background preservation levels

- **Literal:** keep the region photographic and recognizable.
- **Fragmented:** keep two or more faithful source crops that reconstruct its identity.
- **Material continuation:** extend its color, texture class, direction, and light beyond the photo.
- **Graphic reduction:** reduce it to one or two source-specific planes while retaining material and relational cues.

Use literal or fragmented preservation for high-risk interiors. Use material continuation or graphic reduction only when identity still passes the Anywhere test.

## 4. Environmental palette

Map five roles rather than naming one dominant color:

1. **Background base:** the largest contextual field, including its material.
2. **Mid-tone:** the color that connects foreground and background.
3. **Dark anchor:** the deepest structural mass or line.
4. **Light temperature:** the color cast and direction of illumination.
5. **Meaningful accent:** a small color attached to a real subject; allow `none`.

Keep value relationships as well as hue. A pale cool white gallery is not interchangeable with warm cream paper; walnut brown under amber lamps is not interchangeable with beige stock.

When the source mixes interior and exterior light, preserve both temperatures and their boundary. Do not average them into one nostalgic wash.

## 5. Semantic detail map

Judge detail by meaning, not pixel size.

### Preserve

Keep details that identify person, place, use, time, or relationship. Examples: a café menu, a red shop sign, a specific chair color, a cup under a hand, a distinctive window reflection, a worn threshold, or a mountain gap.

### Compress

Merge repeated elements that create density but do not need individual identity. Examples: twenty chairs into three rhythms, leaves into canopy masses, windows into a façade cadence, people into a directional crowd.

### Omit

Remove capture artifacts, accidental edge clutter, redundant micro-texture, and repeated marks that neither identify nor locate the scene.

### Do not invent

Forbid new architecture, brands, captions, weather, dates, landmarks, facial features, decorative objects, or “authentic” clutter not present in the source.

Do not equate `messy` with `meaningless`. In lived-in spaces, clutter may be the subject.

## 6. Field-tone modes

Select one primary field mode.

| Mode | Build from | Best use | Main risk |
| --- | --- | --- | --- |
| `source-tone` | sampled-looking source base color and value | default; most scenes | becoming a flat generic approximation |
| `material-continuation` | source wall, sky, water, wood, snow, or ground | contextual expansion | losing perspective or light boundary |
| `neutral-paper` | source-compatible white, gray, or cream stock | genuine zine/page situations | replacing context with a house style |
| `dark-stock` | source black, charcoal, navy, or brown | night and low-key scenes | crushing dark detail |
| `chromatic-stock` | a real source color | strong color environments | overpowering subjects |
| `raw-photo` | no added stock | documentary/high-risk context | transformation becoming too timid |

Choose `source-tone` when no other mode is clearly better. Use `neutral-paper` only when the source already contains a compatible neutral field or the user requests it.

## 7. Palette modes

### Native

Introduce no new hue. Preserve source temperature and value structure. Use by default.

### Source amplification

Enlarge, repeat, or print a color already owned by a meaningful object. Keep the relationship obvious.

### Tonal translation

Translate colors within their existing family: walnut → umber, off-white plaster → warm white, near-black → charcoal. Preserve relative temperature, value, and saturation.

### Graphic counterpoint

Add exactly one hue not already present. Require all of the following:

- assign one visible function: focal reinforcement, counterweight, eye path, boundary bridge, or semantic emphasis;
- derive contour or placement from a source feature;
- keep it subordinate to the Scene Lock;
- remove it if the composition still works equally well without it.

Do not use counterpoint to make the output look like a zine.

## 8. Abstraction levels

### Light — default

Preserve most context and materials. Simplify only redundant repetition. Prefer for people, interiors, white spaces, subtle light, signage, and memory-led scenes.

### Medium

Preserve all critical locks and reduce flexible zones into planes, rhythms, or incomplete contours. Prefer for architecture, landscapes, and clear foreground/background separation.

### High

Preserve the semantic minimum, at least three anchors, one context-bearing region, palette structure, and dominant relationship. Use only on explicit request or after confirming that the scene remains identifiable.

Never define abstraction by a fixed percentage of deleted detail. Define it by which semantic classes survive.

## 9. Material and typography modules

### Material

Choose at most one primary treatment:

- raw photographic surface;
- matte source-colored paper;
- neutral paper;
- newsprint;
- selective stencil/duplicator layer;
- photocopy layer;
- cut paper with real-looking fibers.

Use a second treatment only as a small supporting trace. Keep texture local and flat; avoid paper mockup depth.

### Typography

Use one of four modes:

- `none` — default when text adds no memory or hierarchy value;
- `provided` — reproduce user text exactly;
- `visible-source` — reuse legible source metadata only when safe and relevant;
- `authored-phrase` — write one short non-factual phrase grounded in the scene.

Allow place/date/time/weather only when provided by the user or visibly reliable in the source. Never infer exact metadata from appearance.

## 10. Transformation-floor fields

Describe the intended visible structure before generation:

- `route_strength`: `restrained`, `balanced`, or `bold`.
- `structural_operations`: one or more named operations from the route specification. Do not count texture or color treatment.
- `graphic_field_share`: approximate canvas share occupied by visibly designed source-derived fields, gaps, margins, or illustration rather than continuous photography.
- `boundary_crossing`: whether a source-derived contour, fragment, or field crosses an internal composition boundary.
- `continuous_full_frame_photo`: set `false` unless a restrained documentary request explicitly needs an edge-to-edge photographic base.
- `texture_only`: always set `false`; a plan that expects texture-only differentiation is invalid.

The transformation floor protects against the opposite failure from context loss: keeping so many source pixels that the result is only the original photograph with a filter.

## 11. Source-information translation fields

Every major non-photographic field needs a traceable source relationship. Describe each mapping with:

- `field_name`: the designed destination field or mark in the output;
- `source_region`: the exact visible source evidence that supplies its information;
- `translation_mode`: one of `contour`, `silhouette`, `rhythm`, `same-source-crop`, `stencil`, `material-continuation`, `value-continuation`, `reflection-hatch`, `detail-repetition`, or `cut-paper`;
- `continuity_anchor`: the visible edge, axis, color/value relation, direction, overlap, or material behavior that joins the field back to the photographic anchor.

Set `generic_substitutions` to `false`. Generic arrows, circles, diagram marks, botanical ornaments, or detached geometry cannot replace source evidence. Set `untranslated_blank_share` to the approximate fraction of the graphic/non-photo area that carries only breathing room. Keep it at or below 0.70 for Documentary Editorial, 0.50 for Multi-frame Joiner, and 0.40 for Graphic Scene Poster or Gathered Collage.

Minimum field mappings:

| Route | Restrained | Balanced | Bold |
| --- | ---: | ---: | ---: |
| Documentary Editorial | 1 | 1 | 2 |
| Multi-frame Joiner | 1 | 1 | 2 |
| Graphic Scene Poster | 1 | 2 | 3 |
| Gathered Collage | 1 | 2 | 3 |

Paper color, grain, halftone, torn fibers, or ink texture alone does not satisfy a mapping. The translated field must retain a visible fact, rhythm, contour, material cue, or relationship from the source.

## 12. JSON plan contract

Use this shape with `scripts/lint_scene_plan.py`:

```json
{
  "route": "documentary-editorial",
  "route_strength": "balanced",
  "reference_mode": "edit-source",
  "scene_core": {
    "identity_anchors": ["...", "...", "..."],
    "spatial_invariants": ["..."],
    "context_bearing_regions": ["..."],
    "environmental_palette": {
      "background_base": "...",
      "midtone": "...",
      "dark_anchor": "...",
      "light_temperature": "...",
      "meaningful_accent": "none"
    },
    "light_time": ["..."],
    "material_signatures": ["...", "..."],
    "density_character": "layered",
    "memory_cues": ["..."],
    "detail_map": {
      "preserve": ["..."],
      "compress": ["..."],
      "omit": ["..."],
      "do_not_invent": ["..."]
    },
    "flexible_zones": ["..."]
  },
  "field_tone_mode": "source-tone",
  "palette_mode": "native",
  "abstraction_level": "light",
  "photo_share": 0.82,
  "transformation_floor": {
    "structural_operations": [
      "asymmetric-grid",
      "crop-scale-shift"
    ],
    "graphic_field_share": 0.12,
    "boundary_crossing": false,
    "continuous_full_frame_photo": false,
    "texture_only": false
  },
  "information_translation": {
    "fields": [
      {
        "field_name": "wall-derived side margin",
        "source_region": "cool white wall and window mullions",
        "translation_mode": "material-continuation",
        "continuity_anchor": "window verticals continue across the internal crop edge"
      }
    ],
    "untranslated_blank_share": 0.45,
    "generic_substitutions": false
  },
  "introduced_hues": 0,
  "typography": {
    "mode": "none",
    "text": ""
  },
  "final_generation_prompt": "optional"
}
```
