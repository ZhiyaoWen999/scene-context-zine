# Prompt Compiler and Quality Assurance

## Contents

1. Prompt compiler
2. Route-specific clauses
3. Negative constraints
4. Source-comparison protocol
5. Weighted scorecard
6. Targeted regeneration
7. Output rationale

## 1. Prompt compiler

Compile one decisive prompt. Replace brackets with source-specific observations; omit unused options.

```text
[REFERENCE AND ROUTE]
Edit the attached source photograph; it is the authoritative visual reference. Build a [route] composition at [ratio chosen from source/use]. Preserve photographic truth and do not recreate the scene from prose.

[SCENE LOCK]
Keep these identity anchors recognizable: [3–5 anchors]. Preserve these spatial relationships: [invariants]. Keep these context-bearing background regions: [regions and minimum visible form]. Preserve the environmental palette: background [base], mid-tone [midtone], dark anchor [dark], light [temperature/direction], source accent [accent or none]. Preserve [materials], the [density character] character, and these memory cues: [cues].

[ALLOCATION AND OPERATIONS]
Keep approximately [photo share] as truthful source photography. [Describe main anchor, crops/fragments, hierarchy, eye path, and boundary operations.] Transform only these flexible zones: [zones]. Keep [preserve list]; compress [compress list]; omit [omit list]; invent none of [do-not-invent list].

[FIELD, PALETTE, ABSTRACTION]
Use [field-tone mode] derived from [source region/material]. Use [palette mode] and [zero/one] introduced hue. [If one hue: exact relationship, source-derived position/contour, and function.] Use [light/medium/high] abstraction while keeping every Scene Lock readable.

[MATERIAL AND TEXT]
Use [one primary material treatment] only in [localized area], with flat scanned behavior and no mockup depth. [Text mode: no text / reproduce exact wording “…” / source-grounded phrase “…”]. Place text [location/hierarchy/treatment] and keep spelling exact.

[HARD CONSTRAINTS]
Do not replace the background with generic cream or blank paper. Do not change light temperature, sanitize lived-in detail, invent objects or metadata, add unrelated graphics, apply a global print filter, damage faces or landmarks, create heavy paper shadows, add logos or watermarks, or use artist/publication names as style shortcuts.
```

Write source facts before style adjectives. Use one sentence per critical lock when the image model tends to ignore dense lists.

## 2. Route-specific clauses

Add only the selected route clause.

### Documentary Editorial

```text
Organize one dominant source-faithful photograph with an asymmetric grid, source-derived margin, restrained crop, and at most two small detail crops. Let hierarchy come from scale and alignment; keep the environment substantially visible.
```

### Multi-frame Joiner

```text
Assemble three to nine overlapping crops from the same source photograph. Keep the main subject intact in the largest fragment, reconstruct at least one spatial invariant across edges, and vary scale to suggest shifting attention without inventing new viewpoints.
```

### Graphic Scene Poster

```text
Keep one landmark or spatial axis as the photographic anchor. Enlarge one source-derived plane, contour, shadow, road, sky, or sign color to create a strong directional hierarchy while preserving place identity.
```

### Gathered Collage

```text
Keep one truthful photographic anchor or subject cutout. Create one irregular, narrow, fibrous paper handoff and continue one source contour or material across it as a simplified illustration. Keep print effects localized and source-derived.
```

## 3. Negative constraints

Use short, failure-specific constraints. Do not paste the entire list when it would dilute critical instructions.

### Always prohibit

- invented scenery, objects, identities, or factual metadata;
- prompt-only reconstruction without the image reference;
- generic background substitution;
- damaged faces, hands, signs, or landmarks;
- illegible supplied text, logos, CTAs, and watermarks;
- mockup framing or unintended 3D paper depth.

### Prohibit when relevant

- cream paper in white/cool or brown/wood scenes unless source-compatible;
- global RISO, Xerox, sepia, nostalgia, or film wash;
- excessive blank field in context-heavy scenes;
- polished minimalism in lived-in rooms;
- detached geometric accents in source-driven routes;
- duplicated people in joiners;
- uniform torn frames in collages;
- high abstraction on identity anchors;
- exact date, place, or weather when not provided or visible.

## 4. Source-comparison protocol

Compare source and result in this order:

1. **Silhouette and orientation:** verify subject pose, gaze, horizon, path, and large shapes.
2. **Background identity:** locate at least one context-bearing region and check its minimum visible form.
3. **Color roles:** compare background base, mid-tone, dark anchor, light temperature, and meaningful accent.
4. **Material:** verify that wood remains wood-like, cool plaster stays cool, snow remains luminous, glass still carries reflection, and lived-in surfaces retain use.
5. **Density:** compare whether the scene is sparse, orderly, layered, crowded, improvised, weathered, or monumental.
6. **Memory cues:** verify supplied/visible signs, objects, gestures, or metadata.
7. **Transformation:** confirm that the selected route is visible and not merely a texture filter.
8. **Artifacts:** inspect faces, hands, text, repeated fragments, seams, and paper depth.

Pass both normal-scale and thumbnail-scale review. Thumbnail review checks identity and hierarchy; normal-scale review checks factual integrity and artifacts.

## 5. Weighted scorecard

Score for diagnosis, but apply critical failures first.

### Critical fail — regenerate regardless of score

- source photo was not used as editing reference;
- core subject or landmark is unrecognizable;
- all context-bearing regions are gone;
- background base or light temperature contradicts the source;
- a person, sign, place, or supplied text is materially falsified;
- invented factual metadata appears.

### Score out of 100

| Dimension | Points | Pass evidence |
| --- | ---: | --- |
| Identity anchors | 15 | at least three recognizable |
| Spatial invariants | 10 | all critical relationships intact |
| Context-bearing background | 15 | one or more regions survive meaningfully |
| Palette and light | 10 | five roles remain coherent |
| Material and density | 10 | source character remains, no sanitization |
| Route clarity | 15 | selected composition grammar is unmistakable |
| Source-derived transformation | 10 | operations derive from real shapes/relationships |
| Restraint and coherence | 5 | one primary material treatment, no effect pileup |
| Typography/facts | 5 | exact or absent; no invention |
| Technical integrity | 5 | no face, hand, seam, text, or mockup artifact |

Require 80 or more and no critical failure. Treat 80–89 as pass with caution; 90 or more as strong.

## 6. Targeted regeneration

State the observed failure first, then preserve everything else.

### Restore context

```text
Keep the current route and subject treatment. Restore [specific context region] with its [source color/material/light] and keep [memory cue]. Reduce blank or generic paper only where it displaced this region.
```

### Restore palette/light

```text
Keep composition unchanged. Replace the current field with [source background base], restore [light temperature/direction], and remove the introduced wash. Preserve the source dark anchor at [location].
```

### Restore lived-in density

```text
Keep hierarchy and crop. Restore [semantic objects] and the original [layered/crowded/improvised] density. Compress repeated detail only; do not clean or stage the room.
```

### Strengthen route

```text
Preserve all Scene Locks. Strengthen only the [route] grammar by [larger crop contrast / clearer fragment overlap / stronger source-derived plane / more legible torn handoff]. Add no new color, texture, or scenery.
```

### Remove style residue

```text
Preserve scene and composition. Remove global [cream/RISO/Xerox/sepia] treatment and detached graphic accents. Keep one localized material effect at [source-derived region].
```

Regenerate once. If the same critical failure remains, stop and report which lock the image model could not preserve rather than pretending success.

## 7. Output rationale

Use one to three Chinese sentences:

```text
我锁定了[背景/光线/材质/记忆线索]，因此选择[路线]而没有把环境换成统一纸色。画面只对[可变区域]做了[裁切/分割/图形延伸/撕纸]，原场景的[关键关系]仍是视觉锚点。
```

Do not expose hidden reasoning, dump the full prompt, or list every parameter unless the user asks.
