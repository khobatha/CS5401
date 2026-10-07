# CS5401 — Special Topics in Computer Science

Code and supporting material for live course demonstrations and starter snippets that students can edit.

## Repository structure

```text
CS5401/
├── course-materials/ # Imported course code and adaptation guidance
├── live-coding/       # Examples developed or demonstrated during class
├── student-snippets/  # Starter code for students to complete or modify
└── resources/        # Shared sample data, diagrams, and reference material
```

## Organizing course material

- Create a folder for each session or topic inside `live-coding/` and `student-snippets/`, as needed.
- Use matching names for related material, such as `01-topic-name/`.
- Keep each example self-contained, with its code, dependencies, and a short README describing how to run it.
- In student snippets, explain the task, mark intended edit points with `TODO` comments, and describe the expected result or checks.
- Put reusable supporting files in `resources/`; keep files used by only one example alongside that example.

## For students

Open the relevant folder in `student-snippets/`, read its README, and follow the setup and editing instructions. Use `live-coding/` to revisit examples covered in class.

The repository is language-neutral. Each example should specify its required language version and tools.

## Generative Deep Learning

The code for David Foster's *Generative Deep Learning, 2nd Edition* is included directly in [course-materials/generative-deep-learning](course-materials/generative-deep-learning/). It is available with a normal clone of CS5401 and can be customized here for the course.

Read the [CS5401 course guide](course-materials/README.md) for setup, customization, attribution, and upstream updates.
