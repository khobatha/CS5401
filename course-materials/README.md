# CS5401 course materials

## Generative Deep Learning, 2nd Edition

[generative-deep-learning/](generative-deep-learning/) contains the code accompanying David Foster's *Generative Deep Learning, 2nd Edition*, imported from [davidADSP/Generative_Deep_Learning_2nd_Edition](https://github.com/davidADSP/Generative_Deep_Learning_2nd_Edition).

The initial import uses upstream commit `9b1048dbe0d698b486ed16d529cf16fcd3aea29d` from `main`. The source is included as a Git subtree with squashed upstream history. Students receive the files with a normal CS5401 clone; no submodule initialization or separate fork is required.

The original [README](generative-deep-learning/README.md), [Apache 2.0 license](generative-deep-learning/LICENCE), and source notices are preserved. The initial import does not modify the upstream examples.

## Student setup

Start with the upstream [setup instructions](generative-deep-learning/README.md) and [Docker guide](generative-deep-learning/docs/docker.md). Run their commands from the imported directory, not the CS5401 repository root:

```bash
cd course-materials/generative-deep-learning
cp sample.env .env
# Edit .env with your local settings and any required Kaggle credentials.
docker compose build
docker compose up
```

The `.env` file is ignored by Git. Keep credentials private. See the upstream README for GPU setup and dataset downloads. The [notebooks](generative-deep-learning/notebooks/) are organized by chapter and example. Download datasets only when needed for the assigned exercise.

## Course customizations

Edit and commit the imported files directly in CS5401. Record the purpose of each adaptation in its commit and add a dated CS5401 modification note in modified source files or a Markdown cell in modified notebooks. Preserve existing attribution and license notices.

Keep exercise instructions and starter snippets in [student-snippets](../student-snippets/) and classroom demonstrations in [live-coding](../live-coding/), linking to the relevant imported notebooks. Avoid committing downloaded datasets, trained model weights, credentials, and generated training outputs.

## Updating from upstream

Use a clean working tree and a review branch. From the CS5401 repository root, fetch upstream into a named reference and merge it through the subtree:

```bash
git switch -c update/generative-deep-learning
git fetch https://github.com/davidADSP/Generative_Deep_Learning_2nd_Edition.git main:refs/remotes/gdl-upstream/main
git subtree merge --prefix=course-materials/generative-deep-learning refs/remotes/gdl-upstream/main --squash
```

Resolve any conflicts while retaining the intended course adaptations, review the changes, and run the affected exercises before merging the update into `main`.
