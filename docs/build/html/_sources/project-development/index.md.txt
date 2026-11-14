---
author: Jia Jun Li
---

# Project Development

The UAV-E Simulator project aims to develop a modular simulation framework for vision-based formation flight with multiple unmanned aircraft. The simulator will provide a controlled environment in which autonomous flight software can use synthetic camera observations to detect and track other aircraft and evaluate formation-keeping behavior before physical flight tests.
The framework will integrate existing simulation technologies instead of developing a simulator from scratch. Realistic fixed-wing dynamics, configurable camera and environmental conditions, and multi-aircraft support are key requirements because they affect how well vision-based formation experiments translate to real flight.
This section documents the project's objectives and development proposal. Architecture decisions, benchmark results, implementation details, and validation evidence will be added as work progresses.

```{toctree}
:maxdepth: 2
:caption: Project Development

project-overview
proposal
```