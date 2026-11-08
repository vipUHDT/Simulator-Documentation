# UHDT Simulator Documentation

Documentation for the **University of Hawaiʻi Drone Technologies (UHDT)** simulator project. This repository is a shared knowledge base for current contributors and future students working on the simulator. It covers project planning, simulator setup, architecture, usage, development, and references.

The website is built using **[Sphinx](https://www.sphinx-doc.org/)**. Pages are written in **Markdown** using **[MyST Parser](https://myst-parser.readthedocs.io/)**, and the HTML site uses the **[Shibuya](https://shibuya.lepture.com/)** theme.

> **New contributors:** You do **not** need to understand Sphinx to edit most pages. In general, edit or create a `.md` file, link it in the appropriate section's `index.md`, build the site, and submit a pull request.

## 1. Repository layout

```text
Simulator-Documentation-main/
├── README.md                     # This contributor guide
├── requirements.txt              # Python dependencies for documentation
├── .gitignore                    # Local/generated files excluded from Git
└── docs/
    ├── Makefile                  # Sphinx build commands on Linux/macOS
    ├── make.bat                  # Sphinx build commands on Windows
    ├── source/                   # EDIT THESE: documentation source files
    │   ├── conf.py               # Sphinx extensions, theme, project settings
    │   ├── index.md              # Homepage and main navigation
    │   ├── _static/              # Logos, icons, and other static assets
    │   ├── project-development/  # Proposals, requirements, evaluations
    │   ├── getting-started/      # Setup and troubleshooting
    │   ├── architecture/         # Components and system interfaces
    │   ├── guides/               # How-to guides and examples
    │   ├── developer/            # Development and maintenance notes
    │   └── reference/            # References and resources
    └── build/                    # GENERATED HTML; do not edit or commit
```

Some sections are still works in progress. Add information as it is tested and verified; do not treat an empty page as a completed guide.

## 2. First-time setup

You need **Python 3**, **Git**, and a terminal. The commands below are run from the **repository root**, unless otherwise noted.

### Clone the repository

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_DIRECTORY>
```

Replace the placeholders with the actual repository URL and its local directory name.

### Create a Python virtual environment (recommended)

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If your shell blocks activation, you can invoke the virtual environment's Python directly or consult your organization's shell policy. Avoid modifying system-wide Python packages just to build the docs.

## 3. Build and view the documentation

Run the following commands from the repository root.

**All platforms (recommended):**

```bash
python -m sphinx -b html docs/source docs/build/html
```

**Alternative: Linux / macOS:**

```bash
cd docs
make html
```

**Alternative: Windows Command Prompt / PowerShell:**

```powershell
cd docs
.\make.bat html
```

Then open `docs/build/html/index.html` in a browser. The `docs/build/` folder is generated automatically; do **not** edit its HTML files. Changes should be made under `docs/source/` and rebuilt.

To check for broken documentation references and other warnings, run from the repository root:

```bash
python -m sphinx -b html -n -W --keep-going docs/source docs/build/html
```

This stricter check treats warnings as errors. It is a useful final check before opening a pull request.

## 4. Editing existing pages

1. Find the relevant `.md` file under `docs/source/`.
2. Edit the Markdown in VS Code or another text editor.
3. Save your changes and build the site using the command in Section 3.
4. Review the rendered page in your browser to check headings, images, links, and code blocks.
5. Commit and submit the changes using the workflow in Section 7.

**Basic Markdown example:**

````markdown
# Running a Simulation

Explain what this page covers.

## Prerequisites

- Install the required simulator software.
- Verify the configuration files.

## Procedure

1. Open a terminal.
2. Run the command:

   ```bash
   echo "Replace with the actual simulation command"
   ```

## Expected result

Describe what a successful run looks like.

## Troubleshooting

Describe common problems and their fixes.
````

Use clear headings and include enough context for someone who was **not** present when the work was done.

## 5. Adding a new page or section

### Add a page within an existing section

For example, to document camera configuration:

1. Create `docs/source/guides/camera-configuration.md`.
2. Write the new page using Markdown.
3. Open `docs/source/guides/index.md`.
4. Add the new file's path **without `.md`** to the section's `toctree` directive. If there is no `toctree`, add one.

Example `docs/source/guides/index.md`:

````markdown
# User Guides

```{toctree}
:maxdepth: 2

usage
camera-configuration
```
````

The actual index may contain additional entries; **keep those entries** when adding yours. Use the real filename and spelling consistently. Sphinx's `toctree` determines which pages appear in the navigation. An unlisted page may build but not appear in the sidebar.

### Add a new top-level section

1. Create a new directory inside `docs/source/`, e.g. `testing/`.
2. Add `testing/index.md` with a heading and its own `toctree` for child pages.
3. Add `testing/index` to the main `toctree` in `docs/source/index.md`.
4. Optionally add a homepage card to `docs/source/index.md`, following the existing MyST `grid` / `grid-item-card` examples.
5. Build the site and verify navigation.

### Link to other pages and add images

Prefer normal Markdown for prose. For links to other documentation pages, use a relative Markdown link or a MyST document reference:

````markdown
[Project overview](../project-development/project-overview.md)

{doc}`../project-development/project-overview`
````

Place shared images in `docs/source/_static/` and reference them with a path relative to the current `.md` file, for example from `docs/source/guides/camera-configuration.md`:

```markdown
![Description of the diagram](../_static/camera-diagram.png)
```

Only reference image files that have actually been added to the repository. Use descriptive alternative text for accessibility. Avoid committing large videos, datasets, build artifacts, or proprietary files directly into the documentation repository.

## 6. Writing guidelines

The purpose of this repository is to make the project reproducible and maintainable, not just to record what the current team remembers.

- **Write for the next student.** Explain the goal, prerequisites, exact steps, expected outcome, and how to debug failures.
- **Be specific.** Record software versions, operating system, hardware, file paths, settings, and tested commands where they matter.
- **Distinguish facts from plans.** Mark incomplete or unverified work clearly as `WIP`, `Planned`, or `Not yet tested`.
- **Keep a consistent structure.** Use one `#` page title, `##` sections, numbered procedures, and fenced code blocks with a language label (e.g. `bash`, `python`, `yaml`).
- **Explain decisions.** For design tradeoffs or simulator comparisons, document the options considered, criteria, evidence, and reason for the decision.
- **Include validation.** When documenting experiments, state the test environment, method, inputs, measurements, results, and limitations. Link to datasets or scripts instead of copying huge outputs into the docs.
- **Credit sources.** Link to vendor documentation, papers, and upstream code when relevant; do not paste unlicensed text or images.
- **Avoid secrets.** Never commit passwords, keys, tokens, private credentials, or sensitive configuration data.
- **Check consistency.** Use consistent terminology and SI units (for example, m, m/s, Hz), and ensure commands match what was actually tested.

## 7. Git and collaboration workflow

To prevent multiple contributors from accidentally overwriting each other's work, use **feature branches and pull requests** rather than pushing directly to `main`.

### Start a new change

From the repository root:

```bash
git switch main
git pull origin main
git switch -c docs/camera-setup
```

Choose a short, descriptive branch name, such as `docs/simulator-comparison` or `docs/fix-installation`.

### Make changes, preview, and commit

```bash
# After editing docs/source/... and rebuilding:
python -m sphinx -b html -n -W --keep-going docs/source docs/build/html

git status
git add README.md docs/source/  # Include only paths you actually changed
git commit -m "docs: add camera setup instructions"
git push -u origin docs/camera-setup
```

The `git add` line is an **example**, not a requirement to stage every documentation page. You can stage individual files with `git add <path>`. Confirm with `git status` that generated files and unrelated changes are not included.

Open a pull request on the repository hosting service and ask a teammate to review it. After approval, merge it into `main`; then update your local `main` before beginning the next task.

### When reviewing a pull request

Check that the instructions are understandable to a new member, all added pages appear in navigation, commands and links work, screenshots are legible, and the documentation builds without unexpected warnings. For changes that describe operational behavior, verify the procedure when possible.

### Avoid merge conflicts

Coordinate when editing shared files such as `docs/source/index.md`, section-level `index.md` files, or `docs/source/conf.py`. Keep each pull request focused. If `main` changes while you work, fetch and merge or rebase it according to the team's chosen Git workflow, then resolve conflicts locally before merging.

## 8. Where to make configuration changes

| What you want to change | File or directory |
| --- | --- |
| Homepage text and top-level navigation | `docs/source/index.md` |
| Section-level navigation | `docs/source/<section>/index.md` |
| Page content | `docs/source/**/*.md` |
| Project name, extensions, theme, logo, favicon | `docs/source/conf.py` |
| Images and other static assets | `docs/source/_static/` |
| Python documentation dependencies | `requirements.txt` |
| Build commands | `docs/Makefile`, `docs/make.bat` |

The current Sphinx configuration uses `myst_parser`, `sphinx.ext.autodoc`, `sphinx.ext.napoleon`, `sphinx.ext.viewcode`, `sphinx_favicon`, and `sphinx_design`. The `shibuya` theme and MyST `colon_fence` feature are also enabled. When adding a new Sphinx extension, update both `docs/source/conf.py` and `requirements.txt` when a separate package is required.


## 9. Useful references

- [Sphinx documentation](https://www.sphinx-doc.org/en/master/)
- [MyST Markdown guide](https://myst-parser.readthedocs.io/en/latest/)
- [Sphinx Design components (cards, grids, tabs)](https://sphinx-design.readthedocs.io/en/latest/)
- [Shibuya theme documentation](https://shibuya.lepture.com/)
- [GitHub guide to pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)

**Maintenance principle:** If you change how the simulator is installed, configured, run, tested, or evaluated, update the relevant documentation whenever possible.
