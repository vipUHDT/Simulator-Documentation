---
author: Jia Jun Li
---

# Project Overview

---
## Background and Motivation
Vision-based formation flight requires an unmanned aircraft to observe other aircraft through onboard cameras and use those observations to support relative positioning and coordinated flight. Testing these behaviors exclusively in the real world can be costly and carries operational risk, particularly when multiple aircraft must fly near one another.
Simulation offers a repeatable setting for developing perception and formation-flight software before flight testing. However, differences between simulated and real-world imagery, aircraft dynamics, and environmental conditions can affect how well algorithms transfer to real aircraft. The UAV-E Simulator aims to reduce this sim-to-real gap, with particular attention to the factors that influence camera-based tracking and formation behavior.
Instead of creating a new simulation engine, the project will select and integrate existing platforms to support these requirements.

## Project Objective
Develop a high-fidelity, modular, multi-UAV simulation framework for developing and testing vision-based formation flight. The framework will produce configurable synthetic camera observations while modeling aircraft dynamics and operating conditions sufficiently well to support repeatable evaluation of perception and autonomous flight software.

## Primary Case: Vision-Based Formation Flight
The intended workflow is to simulate multiple aircraft, generate camera views from one or more vehicles, and deliver these observations to the relevant perception and autonomy software. The software can then be evaluated on its ability to observe other aircraft and support formation-keeping behavior.

The simulator should enable tests of:
- **Aircraft detection and tracking:** Whether vision software can identify and consistently track another aircraft in the camera view.
- **Relative-state estimation:** How accurately image-based methods estimate relative position or orientation, where supported by the perception pipeline.
- **Formation keeping:** How a flight-control or autonomy system maintains a desired relative arrangement using the available observations.
- **Robustness:** How performance changes with lighting, background, camera configuration, aircraft motion, and environmental disturbances.
These are intended evaluation scenarios, not claims of currently implemented functions or achieved accuracy.

## Proposed Capabilities
- **Multi-aircraft simulation:** Concurrent aircraft instances for leader–follower and other formation configurations.
- **Synthetic camera output:** Configurable viewpoints and camera characteristics for vision-based detection and tracking.
- **Fixed-wing dynamics:** Aircraft responses to control commands and disturbances that influence relative motion and image observations.
- **Autonomy integration:** Interfaces for simulated camera feeds, vehicle states, and flight-control software.
- **Configurable environments:** Lighting, terrain, obstacles, and wind to vary the difficulty and realism of formation scenarios.
- **Modular vehicle and sensor models:** Custom airframes, payloads, and potentially additional sensors such as LiDAR and IMUs as project requirements demand.

