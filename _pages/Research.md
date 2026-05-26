---
title: ""
permalink: /Research/
tags: [locomotion, numerical optimization, planning]
header:
classes: wide
mathjax: "true"
---

My research lies at the intersection of **control**, **optimization**, and **machine learning**, highlighting a strong degree of **multidisciplinarity**. My work has evolved from low-level controllers to whole-body control, model identification, and uncertainty-aware motion planning based on optimization techniques for real-world applications. I am particularly known for my pioneering contributions to heuristic locomotion strategies for quadruped robots operating in rough terrain.

More recently, I have steered my research toward hybrid approaches combining AI and model-based techniques for motion planning, while also exploring innovative robotic platforms such as a rappelling robot for hydro-geological risk mitigation and systems for cooperative aerial transportation and manipulation. Driven by the department’s research interests, I have also begun investigating planning and control strategies for tracked robots in agricultural applications.

Below, I summarize in greater detail the research topics I have been involved in during the 2022–2026 period. Wherever applicable, hyperlinks to supervised student theses are provided next to each topic title.

## Reinforcement Learning for Legged Robots

### Model Predictive Shielding — Safe RL

Research on safety-critical locomotion control for quadruped robots under large external disturbances using Model Predictive Safety (MPS) frameworks. Developed adaptive switching strategies between nominal locomotion policies and robust backup policies to preserve robot balance and guarantee recovery. Proposed a learned probabilistic safety value function to predict loss of stability and estimate recoverability without computationally expensive rollout simulations, enabling real-time implementation on physical platforms.

### Residual Learning

Research on distributed sensing and adaptive learning for quadruped locomotion, introducing a multi-IMU architecture with link-mounted inertial sensors to improve perception of localized contact interactions and unmodeled dynamics. Developed online learning frameworks combining proprioceptive and temporal IMU data to estimate contact events, slippage, payload variations, and actuator friction, enabling real-time compensation of modeling errors and improved robustness during dynamic locomotion.

### Guided RL for Aerial Motions  
*(Theses: [Bussola](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/bussola_msc_thesis.pdf), [Roscia](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/roscia23PhdThesis.pdf))*

Research on Guided Reinforcement Learning approaches for generating optimal jumping motions by integrating physics-informed priors into the learning process. The proposed formulation targets the specific task of jumping by restricting the RL action space through physically informed parameterizations, resulting in a more structured policy space while still leveraging existing learning methodologies.

Compared to standard end-to-end approaches, the method reduces the search space, improves sample efficiency, and requires significantly less reward engineering. Landing is achieved using a model-based reactive planner, which continuously recalculates foothold locations to bring the robot to a stop without rebounding.

## Loco-manipulation  
Research on loco-manipulation with centaur robots in contact-rich environments, with particular focus on non-prehensile interaction tasks involving pushing and physical assistance (e.g., wheelchairs). This research investigates hybrid control architectures combining sampling-based Model Predictive Control (MPPI) and online parameter estimation for *simultaneous* motion control and inference of object properties such as mass, inertia, and friction.

Proposed a unified rollout-based framework capable of adapting robot behavior online without predefined contact schedules or force sensing. The work addresses key challenges in contact-rich robotics, including intermittent contacts, hybrid dynamics, and online adaptation to unknown payloads and interaction conditions. Particular emphasis is placed on GPU-accelerated simulation and massively parallel rollout evaluation for real-time onboard deployment.

## Agrifood  
Motivated by the challenges posed by an aging population and the urgent need for pesticide reduction, this research studies tracked vehicles for precision agricultural robotics applications. Tracked robots perform better on rough terrain due to the large contact area between the tracks and the ground, but they rely on skid steering for turning.

The complexity of modeling the system, particularly the intricate terramechanics dynamics arising from soil–track interactions, makes the design of theoretically grounded navigation solutions especially challenging. This research investigates slippage-aware planning and control strategies while also enabling smooth transitions between human operator inputs and autonomous control.

## Numerical Optimization

In the field of legged robotics, I aim to address a key research challenge in the use of numerical optimization for trajectory planning. This research investigates methods to concurrently optimize both the sequence of contacts and their duration within a Model Predictive Control (MPC) framework.

Legged robots exhibit hybrid dynamics, and optimization of contact sequences is typically handled using Mixed-Integer approaches, which often suffer from high computational demands. My goal is to investigate parallel optimization techniques to enable real-time computation and deployment on physical robotic platforms.

## Robotics Applied to Construction

I collaborate as a scientific advisor with the robotics company **Address Robotics**, operating in the field of automated construction. Their goal is to employ legged robots and automated cranes for the autonomous assembly of prefabricated elements, enabling continuous progress monitoring while minimizing costly rework operations.

This research proposes a framework to automate a large number of construction-site processes by leveraging:

1. Heavy-duty legged robots capable of navigating challenging construction environments  
2. Automated cranes  
3. AI-driven navigation, coordination, and cooperation strategies  

## Novel Robotic Platforms

In addition to theoretical research, I am actively involved in the prototyping and development of advanced robotic systems for a variety of applications.

### ALPINE Rappelling Robot  
*(Theses: [Hardonk](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/Luca_Hardonk_thesis.pdf), [Malacarne](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/thesisMalacarne26.pdf))*

This research involves the development of robotic platforms combining rope-based locomotion and legged systems to address maintenance and inspection challenges in steep, remote, and hazardous environments.

One of these projects is **ALPINE**, an innovative climbing robot designed to reduce the risks and costs associated with operations on mountain slopes and vertical infrastructures, where human intervention is often dangerous and expensive.

The platform combines rope-assisted locomotion, jumping capabilities, and aerial stabilization to navigate complex environments while carrying heavy tools for tasks such as drilling, inspection, and maintenance. By leveraging optimal control and advanced optimization techniques, planning algorithms are developed to coordinate leg impulses with energy-efficient rope winding and unwinding, together with online model predictive strategies for disturbance rejection during flight.

The project required multidisciplinary expertise spanning mechanical design, pneumatics, electronics, mechatronics, perception, optimization-based motion planning, and remote supervision systems for real-time monitoring and teleoperation. A prototype of the system has been built, and ongoing research currently focuses on the development of a thrust-based control system to stabilize the robot’s orientation during the flight phase.

Another research direction focuses on the development of a bi-level optimization framework combining genetic algorithms and nonlinear optimization for contact scheduling and optimal multi-jump planning of climbing robots. The approach addresses actuator limitations by decomposing large jumps into sequences of smaller feasible motions while accounting for obstacle avoidance and landing quality on complex vertical surfaces and meshes.

### Cooperative Aerial Manipulation  
*(Thesis: [Sangiorgio](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/sangiorgioMscThesis.pdf))*

**CO-FAST** (“Cooperative and Optimization-based Framework for Aerial Manipulation”) introduces a complete framework for the control and planning of cooperative aerial manipulation using swarms of drones connected to loads through motorized cables.

Each UAV is equipped with electrically driven winches that allow adjustment of cable lengths to manipulate the load. This configuration forms a floating-base parallel kinematic structure enabling precise 6D manipulation while simplifying swarm formation control.

The ability to adjust cable lengths introduces additional degrees of freedom, allowing load manipulation (such as orientation or height variations) to be decoupled from the swarm flight configuration. Furthermore, the capability to dynamically modify swarm geometry increases robustness against environmental disturbances such as wind and turbulence, improves aerodynamic efficiency inspired by bird flocking behavior, and enables modulation of the overall system stiffness.

This feature provides unprecedented positioning accuracy when required while also enabling acceleration and deceleration of the load without inducing unwanted oscillations. CO-FAST enables innovative wildfire suppression strategies and has applications in transportation, handling, and automated assembly of loads in construction sites and remote areas.



You can check more about these in my Youtube Research [playlist](https://youtube.com/playlist?list=PLpppns-JGSyKlxNhpuYCevkTBI8-Apn-H&feature=shared)



# Publications

## Journal articles

### 2025
- **Pseudo-Kinematic Trajectory Control and Planning of Tracked Vehicles**. *Robotics and Autonomous Systems*, 2025. [PDF](https://www.sciencedirect.com/science/article/pii/S0921889025003793)
- **Smooth Human-Robot Shared Control for Autonomous Orchard Monitoring with UGVs**. *IEEE Transactions on Automation Science and Engineering*, 2025. [PDF](https://iit-dlslab.github.io/papers/elbou25tase.pdf)
- **ALPINE: a Climbing Robot for Operations in Mountain Environments**. *Robotics and Autonomous Systems*, 2025. [PDF](https://www.sciencedirect.com/science/article/pii/S0921889025000855)

### 2024
- **Efficient Reinforcement Learning for 3D Jumping Monopods**. *Sensors*, 2024. [PDF](https://pmc.ncbi.nlm.nih.gov/articles/PMC11314636/pdf/sensors-24-04981.pdf) 

### 2023
- **Reactive Landing Controller for Quadruped Robots**. *IEEE Robotics and Automation Letters*, 2023. [PDF](https://iit-dlslab.github.io/papers/roscia23ral.pdf)
- **An Efficient Paradigm for Feasibility Guarantees in Legged Locomotion**. *IEEE Transactions on Robotics*, 2023. [PDF](https://arxiv.org/pdf/2011.07967v2)
- **Orientation Control System: Enhancing Aerial Maneuvers for Quadruped Robots**. *Sensors*, 2023. [PDF](https://www.mdpi.com/1424-8220/23/3/1234)
- **Optimization-Based Reference Generator for Nonlinear Model Predictive Control of Legged Robots**. *Robotics*, 2023. [PDF](https://www.mdpi.com/2218-6581/12/1/6)

### 2021
- **Model Predictive Control with Environment Adaptation for Legged Locomotion**. *IEEE Access*, 2021. [PDF](https://doi.org/10.1109/ACCESS.2021.3137685)

### 2020
- **A simple yet effective whole-body locomotion framework for quadruped robots**. *Frontiers in Robotics and AI*, 2020. [PDF](https://hal.science/hal-03005133v2/file/Frontiers20_QuadrupedalWalking.pdf)
- **Feasible Region: an Actuation-Aware Extension of the Support Region**. *IEEE Transactions on Robotics*, 2020. [PDF](https://iit-dlslab.github.io/papers/orsolino20tro.pdf)
- **STANCE: Locomotion Adaptation over Soft Terrain**. *IEEE Transactions on Robotics*, 2020. [PDF](https://iit-dlslab.github.io/papers/fahmi19tro.pdf)
- **Heuristic Planning for Rough Terrain Locomotion in Presence of External Disturbances and Variable Perception Quality**. *Springer Tracts in Advanced Robotics*, 2020. [PDF](https://iit-dlslab.github.io/papers/focchi19star.pdf)
- **Motion Planning for Quadrupedal Locomotion: Coupled Planning, Terrain Mapping and Whole-Body Control**. *IEEE Transactions on Robotics*, 2020. [PDF](https://cmastalli.github.io/publications/locomotion20tro.pdf)
- **Editorial: Bridging the Gap Between the Lab and the Real World: Future Perspectives for Legged Robots**. *Frontiers in Robotics and AI*, 2020. [PDF](https://www.frontiersin.org/articles/10.3389/frobt.2020.629002/full)

### 2019
- **Fast and Continuous Foothold Adaptation for Dynamic Locomotion through CNNs**. *IEEE Robotics and Automation Letters*, 2019. [PDF](https://iit-dlslab.github.io/papers/villarreal19ral.pdf)
- **Passive Whole-Body Control for Quadruped Robots: Experimental Validation over Challenging Terrain**. *IEEE Robotics and Automation Letters*, 2019. [PDF](https://iit-dlslab.github.io/papers/fahmi19ral.pdf)

### 2018
- **Simultaneous Contact, Gait, and Motion Planning for Robust Multi-Legged Locomotion via Mixed-Integer Convex Optimization**. *IEEE Robotics and Automation Letters*, 2018. [PDF](https://iit-dlslab.github.io/papers/aceituno_mastalli17ral.pdf)
- **Application of Wrench-Based Feasibility Analysis to the Online Trajectory Optimization of Legged Robots**. *IEEE Robotics and Automation Letters*, 2018. [PDF](https://iit-dlslab.github.io/papers/orsolino18ral.pdf)

### 2017
- **High-slope Terrain Locomotion for Torque-Controlled Quadruped Robots**. *Autonomous Robots*, 2017. [PDF](https://ihavoutis.github.io/publications/2016/auro2016focchi.pdf)  

### 2016
- **Robot Impedance Control and Passivity Analysis with Inner Torque and Velocity Feedback Loops**. *Control Theory and Technology*, 2016. [PDF](https://iit-dlslab.github.io/papers/focchi16ctt.pdf)
- **Design of the Hydraulically-Actuated, Torque-Controlled Quadruped Robot HyQ2Max**. *IEEE/ASME Transactions on Mechatronics*, 2016. [PDF](https://iit-dlslab.github.io/papers/tmech16semini.pdf)

### 2015
- **Towards Versatile Legged Robots through Active Impedance Control**. *The International Journal of Robotics Research*, 2015. [PDF](https://iit-dlslab.github.io/papers/tmech16semini.pdf)
- **On the Use of Positive Feedback for Improved Torque Control**. *Control Theory and Technology*, 2015. [PDF](https://iit-dlslab.github.io/papers/dallali15ctt.pdf)

### 2014
- **Quadruped Robot Trotting over Irregular Terrain Assisted by Stereo-Vision**. *Intelligent Service Robotics*, 2014. [PDF](https://iit-dlslab.github.io/papers/bazeille14isr.pdf)
- **Magnetorheologically Damped Compliant Foot for Legged Robotic Application**. *Journal of Mechanical Design*, 2014. [PDF](https://iit-dlslab.github.io/papers/kostamo14.pdf)

### 2011
- **Design of HyQ – a Hydraulically and Electrically Actuated Quadruped Robot**. *Journal of Systems and Control Engineering*, 2011. [PDF](https://iit-dlslab.github.io/papers/semini11jsce.pdf)

## Conference papers

### 2024
- **Distributed Robot Perception for Tracked Vehicles**. *Italian Conference on Robotics and Intelligent Machines (I-RIM)*, 2024. [PDF](https://iit-dlslab.github.io/papers/bussola24irim.pdf)
- **ContactNet: Online Multi-Contact Planning for Acyclic Legged Robot Locomotion**. *Ubiquitous Robots*, 2024. [PDF](https://iit-dlslab.github.io/papers/bratta24ur.pdf)

### 2023
- **Locosim: An Open-Source Cross-Platform Robotics Framework**. *CLAWAR*, 2023. [Publisher](https://iit-dlslab.github.io/papers/focchi23clawar.pdf)
- **CLIO: a Novel Robotic Solution for Exploration and Rescue Missions in Hostile Mountain Environments**. *ICRA*, 2023. [PDF](https://arxiv.org/abs/2209.09693)

### 2022
- **Towards a Generic Navigation and Locomotion Control System for Legged Space Exploration**. *ASTRA*, 2022. [PDF](https://iit-dlslab.github.io/papers/sanchez-delgado2025astra.pdf)
- **Foothold Evaluation Criterion for Dynamic Transition Feasibility for Quadruped Robots**. *ICRA*, 2022. [PDF](https://iit-dlslab.github.io/papers/clemente22icra.pdf)

### 2020
- **On the Hardware Feasibility of Nonlinear Trajectory Optimization for Legged Locomotion based on a Simplified Dynamics**. *ICRA*, 2020. [PDF](https://iit-dlslab.github.io/papers/bratta20icra.pdf)

### 2019
- **Brief Introduction to the Quadruped Robot HyQReal**. *I-RIM*, 2019. [PDF](https://iit-dlslab.github.io/papers/bratta20icra.pdf)
- **On the Detection and Localization of Shin Collisions and Reactive Actions in Quadruped Robots**. *CLAWAR*, 2019. [PDF](https://iit-dlslab.github.io/papers/barasuol19clawar.pdf)

### 2017
- **Online Payload Identification for Quadruped Robots**. *IROS*, 2017. [PDF](https://iit-dlslab.github.io/papers/tournois17iros.pdf)
- **A Combined Limit Cycle-Zero Moment Point Based Approach for Omni-Directional Quadrupedal Bounding**. *CLAWAR*, 2017. [PDF](https://iit-dlslab.github.io/papers/orsolino17clawar.pdf)
- **Validation of Computer Simulations of the HyQ Robot**. *CLAWAR*, 2017. [PDF](https://iit-dlslab.github.io/papers/frigerio17clawar.pdf)
- **Heterogeneous Sensor Fusion for Accurate State Estimation of Dynamic Legged Robots**. *Robotics: Science and Systems (RSS)*, 2017. [PDF](https://iit-dlslab.github.io/papers/nobili_camurri2017rss.pdf)
- **Viscosity-based Height Reflex for Workspace Augmentation for Quadrupedal Locomotion on Rough Terrain**. *IROS*, 2017. [PDF](https://iit-dlslab.github.io/papers/focchi17iros.pdf)
- **Trajectory and Foothold Optimization using Low-Dimensional Models for Rough Terrain Locomotion**. *ICRA*, 2017. [PDF](https://iit-dlslab.github.io/papers/mastalli17icra.pdf)

### 2016
- **Towards a Multi-Legged Mobile Manipulator**. *ICRA*, 2016. [PDF](https://iit-dlslab.github.io/papers/icra16brehman.pdf)
- **A Design Method of a Robust Controller for Hydraulic Actuation with Disturbance Observers**. *AMC*, 2016. [PDF](https://iit-dlslab.github.io/papers/kuwahara16acm.pdf)
- **Hierarchical Planning of Dynamic Movements without Scheduled Contact Sequences**. *ICRA*, 2016. [PDF](https://iit-dlslab.github.io/papers/icra16mastalli.pdf)

### 2015
- **Slip Detection and Recovery for Quadruped Robots**. *ISRR*, 2015. [PDF](https://iit-dlslab.github.io/papers/focchi15isrr.pdf)
- **Design of a Hydraulically Actuated Arm for a Quadruped Robot**. *CLAWAR*, 2015. [PDF](https://iit-dlslab.github.io/papers/rehman15clawar.pdf)
- **Planning and Execution of Dynamic Whole-Body Locomotion for a Hydraulic Quadruped on Challenging Terrain**. *ICRA*, 2015. [PDF](https://iit-dlslab.github.io/papers/winkler15icra.pdf)
- **Design Overview of the Hydraulic Quadruped Robots HyQ2Max and HyQ2Centaur**. *14th Scandinavian International Conference on Fluid Power (SICFP)*, 2015.  [PDF](https://iit-dlslab.github.io/papers/semini15sicfp.pdf)

### 2014
- **Path Planning with Force-Based Foothold Adaptation and Virtual Model Control for Torque Controlled Quadruped Robots**. *ICRA*, 2014. [PDF](https://iit-dlslab.github.io/papers/winkler14icra.pdf)

### 2013
- **Local Reflex Generation for Obstacle Negotiation in Quadrupedal Locomotion**. *CLAWAR*, 2013. [PDF](https://iit-dlslab.github.io/papers/focchi13clawar.pdf)
- **Vision Enhanced Reactive Locomotion Control for Trotting on Rough Terrain**. *TePRA*, 2013. [PDF](https://iit-dlslab.github.io/papers/bazeille13tepra.pdf)

### 2012
- **On the Role of Load Motion Compensation in High-Performance Force Control**. *IROS*, 2012. [PDF](https://iit-dlslab.github.io/papers/boaventura12iros.pdf)
- **Design and Scaling of Versatile Quadruped Robots**. *CLAWAR*, 2012. [PDF](https://iit-dlslab.github.io/papers/semini12clawar.pdf)
- **Dynamic Torque Control of a Hydraulic Quadruped Robot**. *ICRA*, 2012. [PDF](https://iit-dlslab.github.io/papers/boaventura12icra.pdf)
- **Torque-Control Based Compliant Actuation of a Quadruped Robot**. *AMC*, 2012. [PDF](https://iit-dlslab.github.io/papers/focchi12acm.pdf)

### 2011
- **Novel Concept for an Air-Pressure Driven Micro-Turbine for Power Generation**. *ASME Turbo Expo*, 2011. [PDF](https://www.researchgate.net/publication/261360745_Novel_Concept_for_an_Air-Pressure_Driven_Micro-Turbine_for_Power_Generation)

### 2010
- **Control of a Hydraulically-Actuated Quadruped Robot Leg**. *ICRA*, 2010. [PDF](https://iit-dlslab.github.io/papers/icra10focchi.pdf)
- **Water/Air Performance Analysis of a Fluidic Muscle**. *IROS*, 2010. [PDF](https://ieeexplore.ieee.org/document/5650432)



>   A brief presentation of my research work can be found  [here](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/ResearchPresentation.pdf)   

>  The video of my talk  for "PI stories" collection of seminars   at University of Trento can be found [here](https://www.youtube.com/watch?v=cxCF_FkHoKU)   

>   The video of my talk at Acquario di Genova on my recent research results can be found  [here](https://youtu.be/UBjLsTrt-54)

>   The video of my talk at the ICRA workshop on Opportunities and Challenges in Space Robotics ([video](https://youtu.be/LYoq4_mGvCQ))

>   The video of my talk at the University of Porto  ([video](https://youtu.be/70j4qgd30GI))
