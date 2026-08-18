# Composition Route Modules

## Contents

1. Selection rules
2. Route A — Documentary Editorial
3. Route B — Multi-frame Joiner
4. Route C — Graphic Scene Poster
5. Route D — Gathered Collage
6. Secondary techniques
7. Route-preview format
8. Distinctness test

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

## 2. Route A — Documentary Editorial

### Intent

Let design organize the scene while the photograph remains the main evidence.

### Use for

- cafés, homes, studios, museums, shops, white galleries, and brown/wood interiors;
- portraits whose surroundings explain the person;
- subtle mixed light, weather, reflections, or material atmosphere;
- scenes with high cost of background loss.

### Grammar

- Keep 65–100% truthful photography.
- Use an asymmetrical grid, restrained crop, margin, thin alignment, or one isolated cutout.
- Keep one dominant photograph; allow one or two small detail crops only when they strengthen memory.
- Derive margins and field tone from the source background.
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

## 3. Route B — Multi-frame Joiner

### Intent

Fragment the view without replacing reality. Let multiple crops reconstruct how the eye moved through the scene.

### Use for

- travel, streets, transit, crowds, tables, complex interiors, and motion;
- sources with several context-bearing regions;
- users who like cutting, splitting, and irregular fragments;
- scenes where one crop cannot hold both subject and place.

### Grammar

- Keep 55–100% source photography across three to nine fragments.
- Keep the main subject intact in the largest fragment unless intentional repetition is safe.
- Use adjacent or overlapping crops from the same source; vary scale modestly.
- Reconstruct at least one spatial invariant across fragment edges.
- Repeat a context cue at most twice to suggest attention or time, not clone noise.
- Allow narrow source-colored gaps, raw overlap, or a contact-sheet strip.
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

## 4. Route C — Graphic Scene Poster

### Intent

Make a designed scene poster in which the landmark or spatial identity remains unmistakable.

### Use for

- architecture, city streets, coastlines, mountains, roads, signage, vehicles, and travel memories;
- sources with a strong silhouette, horizon, diagonal, façade rhythm, or scale contrast;
- requests for more energy and less uniform quietness.

### Grammar

- Keep 40–80% source photography.
- Preserve one large landmark or scene-specific photographic anchor.
- Enlarge one source-derived plane, shadow, road, sky, sign color, or contour.
- Use scale shift, diagonal, crop, and clear hierarchy.
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

### Prompt vocabulary

Use: `source-derived graphic plane`, `landmark-scale photographic anchor`, `asymmetric travel poster`, `cropped photographic scale shift`, `clear directional hierarchy`.

## 5. Route D — Gathered Collage

### Intent

Retain the tactile real-photo/illustration handoff from the original project while removing its fixed background and color defaults.

### Use for

- a clear figure, object, tree, vehicle, building, or horizon that can cross a boundary;
- requests for hand-torn fibers, cutout, paper tactility, selective print, or original Gathered Scenes character;
- sources whose semantic minimum remains strong at 25–60% photography.

### Grammar

- Keep 25–60% truthful source photography.
- Preserve the core subject in the largest photo anchor or cutout.
- Use one irregular hand-torn handoff, not a uniform frame.
- Continue one source shape across photography and illustration.
- Use one primary illustration grammar: silhouette, contour, field, rhythm, or cut-paper.
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

### Prompt vocabulary

Use: `truthful photographic cutout`, `single irregular fibrous handoff`, `source-shape continuation`, `selective printed layer`, `flat tactile paper collage`.

## 6. Secondary techniques

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

## 7. Route-preview format

For each proposed route, return:

```text
Route:
Why it fits:
Locked context:
Photo presence:
Field / palette / abstraction / material:
Main transformation:
Main risk:
```

Make routes materially different. Do not vary only the color.

## 8. Distinctness test

At thumbnail scale:

- Documentary Editorial should read as one dominant truthful scene organized by a quiet grid.
- Multi-frame Joiner should read as a source-only field of shifting attention.
- Graphic Scene Poster should read as a landmark or spatial axis reshaped into a strong graphic hierarchy.
- Gathered Collage should read as a tactile boundary between truthful photography and source-derived paper interpretation.

If two routes differ only by texture, reselect their composition operations.
