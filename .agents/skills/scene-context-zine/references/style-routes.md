# Composition Route Modules

## Contents

1. Selection rules
2. Route strength and transformation floor
3. Anchored synthesis
4. Route A — Documentary Editorial
5. Route B — Multi-frame Joiner
6. Route C — Graphic Scene Poster
7. Route D — Gathered Collage
8. Secondary techniques
9. Route-preview format
10. Distinctness test

## 1. Selection rules

Choose exactly one primary route. Add at most one secondary technique. Let the user's explicit route win unless it conflicts with a Scene Lock.

Use these signals:

| Source condition | Best first choice | Avoid first |
| --- | --- | --- |
| fragile interior context, subtle light, white/brown background | Documentary Editorial | high-abstraction Gathered Collage |
| many meaningful details across the frame | Multi-frame Joiner | large empty paper field |
| landmark, façade, horizon, signage, strong axis | Graphic Scene Poster | timid centered photo |
| clear subject cutout and user wants tactile zine | Gathered Collage | raw-photo-only layout |
| uncertain | Documentary Editorial | style-heavy route |

Define photo share as the approximate area showing truthful source photography, including repeated source crops. Treat ranges as guardrails, not quotas.

## 2. Route strength and transformation floor

Choose one strength before compiling the prompt:

| Strength | Purpose | Minimum structural operations | Result must read as |
| --- | --- | ---: | --- |
| `restrained` | fragile context or explicit low-change request | 1 | clearly organized editorial treatment |
| `balanced` | default | 2 | a new composition built from the source |
| `bold` | explicit differentiation with robust locks | 3 | an unmistakable poster or collage |

Count only structural operations: asymmetric content-derived grid, crop/scale shift, same-source fragment reassembly, source-derived graphic plane, boundary crossing, negative-space reallocation, directional cut, source-detail repetition, or subject cutout. Do not count color grading, grain, halftone, paper texture, saturation, or a border as structural operations.

Use these photo-share guardrails by strength:

| Route | Restrained | Balanced | Bold |
| --- | ---: | ---: | ---: |
| Documentary Editorial | 80–95% | 65–85% | 55–75% |
| Multi-frame Joiner | 75–90% | 55–80% | 45–70% |
| Graphic Scene Poster | 60–75% | 45–65% | 35–55% |
| Gathered Collage | 45–60% | 30–50% | 25–40% |

For balanced/bold output, do not leave one continuous edge-to-edge photograph as the whole composition. For Graphic Scene Poster, require a visibly source-derived graphic field of at least 25% at balanced and 35% at bold. For Gathered Collage, require at least 30% at balanced and 40% at bold. In Graphic Scene Poster and Gathered Collage, make one source-derived form cross an internal boundary.

Every major non-photo field must remain information-bearing. Map it to one exact source region, one translation mode, and one continuity anchor. A source-colored blank may provide limited breathing room, but paper color, texture, or a generic symbol cannot stand in for the wall, water, foliage, reflection, signage, object rhythm, or contour that was displaced.

**Automatic rejection:** if the composition differs from the source only through color, contrast, saturation, grain, halftone, paper texture, or another global/local surface effect, it has not met the transformation floor.

## 3. Anchored synthesis

Use this default fusion for landscapes, architecture, landmarks, and travel scenes. It combines several compatible design traditions as a hierarchy rather than a pile of effects:

1. **Anchor:** keep one place-defining photographic subject or relationship large and truthful.
2. **Grid:** derive an asymmetric layout from the source horizon, façade, path, reflection, gaze, or silhouette.
3. **Field:** convert one flexible source region into a flat source-colored plane that occupies meaningful area.
4. **Energy:** choose either one same-source fragment at a changed scale or one directional cut along a real source axis.
5. **Material:** optionally localize one halftone, dry-ink, or transparent overprint trace to the graphic field only.

Do not use every available operation. At balanced strength, use anchor + grid + field and one energy choice. At bold strength, increase crop contrast or graphic-field area before adding more texture.

## 4. Route A — Documentary Editorial

### Intent

Let design organize the scene while the photograph remains the main evidence.

### Use for

- cafés, homes, studios, museums, shops, white galleries, and brown/wood interiors;
- portraits whose surroundings explain the person;
- subtle mixed light, weather, reflections, or material atmosphere;
- scenes with high cost of background loss.

### Grammar

- Keep 65–85% truthful photography at balanced strength; use the strength table for other modes.
- Use an asymmetrical grid, restrained crop, margin, thin alignment, or one isolated cutout.
- Keep one dominant photograph; allow one or two small detail crops only when they strengthen memory.
- Derive margins and field tone from the source background.
- Carry at least one wall edge, shadow value, window rhythm, tabletop line, or other source cue into the margin; do not make the margin a color-only slab when it replaces context.
- Prefer native palette and light abstraction.
- Use raw-photo, source-tone, or material-continuation fields.
- Keep type small and factual or omit it.

### Character

Quiet does not mean empty. Preserve semantic objects and the density of the actual room. Let hierarchy come from crop and spacing rather than aggressive effects.

### Failure conditions

- the layout looks like an unedited photo with a border;
- a neutral margin changes the room's white balance;
- the crop removes the defining window, wall, or object relationship;
- editorial type becomes a headline unrelated to the moment.

### Prompt vocabulary

Use: `source-faithful editorial page`, `asymmetric grid`, `truthful photographic anchor`, `source-derived margin`, `small mechanical type`, `flat print surface`.

Do not use artist or publication names.

## 5. Route B — Multi-frame Joiner

### Intent

Fragment the view without replacing reality. Let multiple crops reconstruct how the eye moved through the scene.

### Use for

- travel, streets, transit, crowds, tables, complex interiors, and motion;
- sources with several context-bearing regions;
- users who like cutting, splitting, and irregular fragments;
- scenes where one crop cannot hold both subject and place.

### Grammar

- Keep 55–80% source photography across three to nine fragments at balanced strength; use the strength table for other modes.
- Keep the main subject intact in the largest fragment unless intentional repetition is safe.
- Use adjacent or overlapping crops from the same source; vary scale modestly.
- Reconstruct at least one spatial invariant across fragment edges.
- Repeat a context cue at most twice to suggest attention or time, not clone noise.
- Allow narrow source-colored gaps, raw overlap, or a contact-sheet strip.
- Build connective gaps from the source pavement, façade rhythm, rail direction, reflection, or another visible relationship; never insert generic arrows or diagram marks to manufacture motion.
- Prefer native or source-amplification palette.
- Use light to medium abstraction only in connective zones.

### Character

Create a field of attention rather than a broken mosaic. Keep source orientation legible. Use overlap to show sequence, not to hide the scene.

### Failure conditions

- fragments are arbitrary rectangles with no eye path;
- every crop has equal weight;
- the person is duplicated inconsistently or anatomically damaged;
- invented views imply source information that does not exist;
- paper gaps occupy more area than the reconstructed place.

### Prompt vocabulary

Use: `multi-frame photographic assembly`, `overlapping source crops`, `shifted attention`, `reconstructed spatial continuity`, `irregular but legible fragment rhythm`.

Do not request new camera angles that the source cannot support.

## 6. Route C — Graphic Scene Poster

### Intent

Make a designed scene poster in which the landmark or spatial identity remains unmistakable.

### Use for

- architecture, city streets, coastlines, mountains, roads, signage, vehicles, and travel memories;
- sources with a strong silhouette, horizon, diagonal, façade rhythm, or scale contrast;
- requests for more energy and less uniform quietness.

### Grammar

- Keep 45–65% source photography at balanced strength; use the strength table for other modes.
- Preserve one large landmark or scene-specific photographic anchor.
- Reserve at least 25% of the balanced canvas for source-derived graphic fields; use at least 35% at bold strength.
- Enlarge one source-derived plane, shadow, road, sky, reflection, sign color, or contour.
- Give each enlarged plane a visible source fact: contour, value change, material rhythm, same-source crop, or reflection structure. Color alone is insufficient.
- Use an asymmetric grid plus at least one crop/scale shift, same-source fragment, or directional cut.
- Make one real contour, fragment, or plane cross an internal boundary.
- Select source-tone, material-continuation, or chromatic-stock field.
- Prefer source amplification; allow one graphic counterpoint only when structurally necessary.
- Use medium abstraction in flexible zones, not on the landmark.
- Allow a real place name or date when supplied.

### Character

Use the scene to generate the grid. Keep the place readable before the poster treatment becomes visible.

### Failure conditions

- a generic circle, rectangle, or bright dot replaces source geometry;
- the photograph becomes a tiny decorative sticker;
- the landmark loses its proportion or relation to the horizon;
- travel metadata is fabricated;
- the color field is unrelated to the scene.
- the source still fills the canvas continuously and only receives a texture or color treatment.

### Prompt vocabulary

Use: `source-derived graphic plane`, `landmark-scale photographic anchor`, `asymmetric content-derived grid`, `cropped photographic scale shift`, `same-source fragment`, `internal boundary crossing`, `clear directional hierarchy`.

## 7. Route D — Gathered Collage

### Intent

Retain the tactile real-photo/illustration handoff from the original project while removing its fixed background and color defaults.

### Use for

- a clear figure, object, tree, vehicle, building, or horizon that can cross a boundary;
- requests for hand-torn fibers, cutout, paper tactility, selective print, or original Gathered Scenes character;
- sources whose semantic minimum remains strong at 25–60% photography.

### Grammar

- Keep 30–50% truthful source photography at balanced strength; use the strength table for other modes.
- Preserve the core subject in the largest photo anchor or cutout.
- Use one irregular hand-torn handoff, not a uniform frame.
- Continue one source shape across photography and illustration.
- Use one primary illustration grammar: silhouette, contour, field, rhythm, or cut-paper.
- Make every major paper region carry translated source information such as reed rhythm, veil contour, window grid, reflected light, water hatch, foliage mass, or fabric fold; reserve pure blank only as subordinate breathing room.
- Derive paper/field tone from the source; do not default to cream.
- Default to native or source-amplification palette.
- Localize RISO-like, photocopy, halftone, dry ink, or fiber behavior.
- Preserve meaningful background in the photo anchor or as a faithful material continuation.

### Character

Keep the original strengths: figure separation, irregular crop, boundary crossing, paper tactility, and strong hierarchy. Treat negative space and saturated color as optional.

### Failure conditions

- the room, weather, or place becomes generic paper;
- the tear surrounds every edge equally;
- illustration traces the whole photograph;
- all complex detail is erased regardless of meaning;
- an accent hue is added only to recreate a house style.
- paper areas contain only grain or color while the displaced scene information disappears;
- generic arrows, circles, leaves, or diagram symbols appear without a visible source owner.

### Prompt vocabulary

Use: `truthful photographic cutout`, `single irregular fibrous handoff`, `source-shape continuation`, `selective printed layer`, `flat tactile paper collage`.

## 8. Secondary techniques

Add at most one:

### Contact-sheet memory strip

Use two to five crops labeled only with supplied or visible information. Keep it subordinate to the main route.

### Ephemera layer

Use a real ticket, menu, map fragment, date, place name, or sentence supplied by the user. Do not fabricate provenance.

### Selective print layer

Apply one print process to a shadow, window, sky, garment, or source-derived plane. Keep the main photo natural.

### Subject cutout

Separate one person or object and let it cross a grid, fragment, or field boundary. Preserve silhouette, pose, gaze, and scale.

### Illustration continuation

Extend one contour, path, shadow, or material beyond the photographic edge. Do not invent new scenery.

## 9. Route-preview format

For each proposed route, return:

```text
Route:
Why it fits:
Locked context:
Photo presence:
Route strength / transformation floor:
Field / palette / abstraction / material:
Information translation (source → mode → continuity):
Main transformation:
Main risk:
```

Make routes materially different. Do not vary only the color.

## 10. Distinctness test

At thumbnail scale:

- Documentary Editorial should read as one dominant truthful scene organized by a quiet grid.
- Multi-frame Joiner should read as a source-only field of shifting attention.
- Graphic Scene Poster should read as a landmark or spatial axis reshaped into a strong graphic hierarchy.
- Gathered Collage should read as a tactile boundary between truthful photography and source-derived paper interpretation.

If two routes differ only by texture, reselect their composition operations.

Also reject any balanced/bold result that reads as the original full-frame photograph at thumbnail scale. Preserve the scene relationship, but visibly reallocate area, scale, and boundaries.

Finally, point to the source owner of every major graphic field or mark. If one can only be described as “decorative,” remove it or translate a real source cue into that position.
