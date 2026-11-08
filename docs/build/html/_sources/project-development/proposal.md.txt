# Development Proposal
---

## Proposed Approach
The UAV-E Simulator will integrate an existing simulation stack to support **vision-based fixed-wing formation flight**. Simulator selection will be driven by the ability to run multiple aircraft, generate usable camera imagery of other vehicles, interface with perception and flight-control software, and represent the dynamics and environmental effects relevant to formation keeping.
The project will NOT develop a complete simulation engine from scratch. Instead, it will select, configure, extend, and validate existing technologies against the project's requirements.

## Simulator Evaluation
Candidates will undergo an initial capability screen followed by a quantitative comparison of feasible options. Criteria from prior UAV simulation research will be adapted to emphasize the primary mission: testing camera-based aircraft tracking and formation flight.
```{note}
For more please look at the DMM Section
```
## Development Phases
1. Define formation-flight requirements and research current implementations of UAV simulators.
2. Screen and benchmark simulators: Shortlist candidates and compare perception-relevant rendering, fixed-wing support, multi-UAV support, runtime performance, and integration.
3. Integrate a baseline fixed-wing aircraft: Establish flight-dynamics and autopilot/software communication for one aircraft.
4. Add camera and perception integration: Produce synthetic camera imagery and connect it to the vision-based tracking software.
5. Enable multi-aircraft formation scenarios: Add multiple controllable aircraft, relative-motion scenarios, and formation-control integration.
6. Introduce environmental variation and validate: Test lighting, backgrounds, wind, and other variables. Implement unsupervised automated testing for changing variables. Compare relevant outputs to real-world data where available.
```{note}
Phases may overlap and will be refined after simulator selection.
```
## Deliverables
- Documented simulator selection criteria, benchmarks, and architecture rationale.
A baseline fixed-wing simulation connected to the chosen flight software.
- Synthetic camera output suitable for integration with a vision-based aircraft-tracking pipeline.
- Repeatable multi-UAV formation scenarios.
Measurements of perception, runtime, and formation-test performance, as supported by the implemented system.
- Validation findings and documentation of remaining sim-to-real limitations.