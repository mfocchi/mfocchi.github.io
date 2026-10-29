---
title: ""
permalink: /Research/
tags: [locomotion, numerical optimization, planning]
header:
classes: wide
mathjax: "true"
---

<style>
.research-tabbar { display: flex; flex-wrap: wrap; gap: .4em; margin: 1.5em 0 1em; padding-bottom: .8em;
  border-bottom: 1px solid rgba(128,128,128,.35); }
.research-tabbar button { font: inherit; font-size: .8em; color: inherit; background: transparent; cursor: pointer;
  padding: .45em .9em; border: 1px solid rgba(128,128,128,.45); border-radius: 999px; opacity: .8; }
.research-tabbar button:hover { opacity: 1; }
.research-tabbar button[aria-selected="true"] { opacity: 1; font-weight: bold; background: rgba(128,128,128,.25);
  border-color: currentColor; }
.research-tabbar .n { opacity: .65; margin-left: .3em; font-weight: normal; }
.research-js .research-panel { display: none; }
.research-js .research-panel.active { display: block; }
.research-js .research-panel > h1:first-child { display: none; }
/* research topics: sub-tabs and separation */
.topic-tabbar { display: flex; flex-wrap: wrap; gap: .35em; margin: .2em 0 1.4em; }
.topic-tabbar button { font: inherit; font-size: .72em; color: inherit; background: transparent; cursor: pointer;
  padding: .3em .8em; border: 1px dashed rgba(128,128,128,.5); border-radius: 999px; opacity: .8; }
.topic-tabbar button:hover { opacity: 1; }
.topic-tabbar button[aria-pressed="true"] { opacity: 1; font-weight: bold; border-style: solid; border-color: currentColor; }
.topic-tabbar button:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
.topic { border-top: 1px solid rgba(128,128,128,.35); margin-top: 2.4em; padding-top: .2em; }
.topic > h2 { margin-top: .9em; padding-left: .55em; border-left: 4px solid currentColor; border-bottom: 0; }
.topic h3 { font-size: 1em; margin: 1.4em 0 .4em; padding-bottom: .2em; border-bottom: 1px dotted rgba(128,128,128,.45); }
.topic-filtered .topic-intro { display: none; }
.topic-filtered .topic { display: none; border-top: 0; margin-top: 0; }
.topic-filtered .topic.on { display: block; }
.topic-filtered .topic.on > h2 { margin-top: 0; }
/* paper links: PDF / Video / BibTeX */
.research-panel li > a, .bib-btn { display: inline-block; font: inherit; font-size: .72em; line-height: 1.4; color: inherit;
  background: transparent; text-decoration: none; cursor: pointer; padding: .1em .65em; margin: .15em .1em 0 0;
  border: 1px solid rgba(128,128,128,.5); border-radius: 999px; opacity: .85; vertical-align: .1em; }
.research-panel li > a:hover, .bib-btn:hover { opacity: 1; border-color: currentColor; }
.research-panel li > a:focus-visible, .bib-btn:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
.bib-all { font-size: .8em; margin: -.4em 0 1.2em; }
#bib-dialog { width: min(46rem, calc(100vw - 2rem)); padding: 0; border: 1px solid rgba(128,128,128,.45);
  border-radius: 8px; background: #252a34; color: #eaeaea; }
#bib-dialog::backdrop { background: rgba(0,0,0,.6); }
#bib-dialog header { display: flex; align-items: center; gap: .6em; padding: .6em .9em; border-bottom: 1px solid rgba(128,128,128,.35); }
#bib-dialog header strong { flex: 1; font-size: .8em; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
#bib-dialog header button { font: inherit; font-size: .75em; color: inherit; background: transparent; cursor: pointer;
  padding: .3em .8em; border: 1px solid rgba(128,128,128,.5); border-radius: 999px; }
#bib-dialog header button:hover { border-color: currentColor; }
#bib-dialog pre { margin: 0; padding: .9em; max-height: 60vh; overflow: auto; font-size: .7em; line-height: 1.5;
  white-space: pre-wrap; overflow-wrap: anywhere; background: transparent; }
</style>

<div class="research-tabbar" id="research-tabbar" role="tablist" hidden><button type="button" role="tab" data-tab="topics" aria-selected="false">Topics</button><button type="button" role="tab" data-tab="journals" aria-selected="false">Publications (Journals)<span class="n">27</span></button><button type="button" role="tab" data-tab="conferences" aria-selected="false">Publications (Conferences)<span class="n">34</span></button></div>

<div class="research-panel" id="research-topics" markdown="1">

# Research topics

<div class="topic-tabbar" id="topic-tabbar" role="group" aria-label="Filter research topics" hidden><button type="button" data-topic="all" aria-pressed="true">All topics</button><button type="button" data-topic="rl" aria-pressed="false">Reinforcement learning</button><button type="button" data-topic="locomanipulation" aria-pressed="false">Loco-manipulation</button><button type="button" data-topic="agrifood" aria-pressed="false">Agrifood</button><button type="button" data-topic="optimization" aria-pressed="false">Numerical optimization</button><button type="button" data-topic="construction" aria-pressed="false">Construction</button><button type="button" data-topic="platforms" aria-pressed="false">Novel platforms</button></div>

<div class="topic-intro" markdown="1">

My research lies at the intersection of **control**, **optimization**, and **machine learning**, highlighting a strong degree of **multidisciplinarity**. My work has evolved from low-level controllers to whole-body control, model identification, and uncertainty-aware motion planning based on optimization techniques for real-world applications. I am particularly known for my pioneering contributions to heuristic locomotion strategies for quadruped robots operating in rough terrain.

More recently, I have steered my research toward hybrid approaches combining AI and model-based techniques for motion planning, while also exploring innovative robotic platforms such as a rappelling robot for hydro-geological risk mitigation and systems for cooperative aerial transportation and manipulation. Driven by the department’s research interests, I have also begun investigating planning and control strategies for tracked robots in agricultural applications.

Below, I summarize in greater detail the research topics I have been involved in during the 2022–2026 period. Wherever applicable, hyperlinks to supervised student theses are provided next to each topic title.

</div>

<section class="topic" id="topic-rl" markdown="1">

## Reinforcement Learning for Legged Robots

### Model Predictive Shielding — Safe RL

Research on safety-critical locomotion control for quadruped robots under large external disturbances using Model Predictive Safety (MPS) frameworks. Developed adaptive switching strategies between nominal locomotion policies and robust backup policies to preserve robot balance and guarantee recovery. Proposed a learned probabilistic safety value function to predict loss of stability and estimate recoverability without computationally expensive rollout simulations, enabling real-time implementation on physical platforms.

### Residual Learning

Research on distributed sensing and adaptive learning for quadruped locomotion, introducing a multi-IMU architecture with link-mounted inertial sensors to improve perception of localized contact interactions and unmodeled dynamics. Developed online learning frameworks combining proprioceptive and temporal IMU data to estimate contact events, slippage, payload variations, and actuator friction, enabling real-time compensation of modeling errors and improved robustness during dynamic locomotion.

### Guided RL for Aerial Motions  
*(Theses: [Bussola](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/bussola_msc_thesis.pdf), [Roscia](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/thesis/roscia23PhdThesis.pdf))*

Research on Guided Reinforcement Learning approaches for generating optimal jumping motions by integrating physics-informed priors into the learning process. The proposed formulation targets the specific task of jumping by restricting the RL action space through physically informed parameterizations, resulting in a more structured policy space while still leveraging existing learning methodologies.

Compared to standard end-to-end approaches, the method reduces the search space, improves sample efficiency, and requires significantly less reward engineering. Landing is achieved using a model-based reactive planner, which continuously recalculates foothold locations to bring the robot to a stop without rebounding.

</section>

<section class="topic" id="topic-locomanipulation" markdown="1">

## Loco-manipulation  
Research on loco-manipulation with centaur robots in contact-rich environments, with particular focus on non-prehensile interaction tasks involving pushing and physical assistance (e.g., wheelchairs). This research investigates hybrid control architectures combining sampling-based Model Predictive Control (MPPI) and online parameter estimation for *simultaneous* motion control and inference of object properties such as mass, inertia, and friction.

Proposed a unified rollout-based framework capable of adapting robot behavior online without predefined contact schedules or force sensing. The work addresses key challenges in contact-rich robotics, including intermittent contacts, hybrid dynamics, and online adaptation to unknown payloads and interaction conditions. Particular emphasis is placed on GPU-accelerated simulation and massively parallel rollout evaluation for real-time onboard deployment.

</section>

<section class="topic" id="topic-agrifood" markdown="1">

## Agrifood  
Motivated by the challenges posed by an aging population and the urgent need for pesticide reduction, this research studies tracked vehicles for precision agricultural robotics applications. Tracked robots perform better on rough terrain due to the large contact area between the tracks and the ground, but they rely on skid steering for turning.

The complexity of modeling the system, particularly the intricate terramechanics dynamics arising from soil–track interactions, makes the design of theoretically grounded navigation solutions especially challenging. This research investigates slippage-aware planning and control strategies while also enabling smooth transitions between human operator inputs and autonomous control.

</section>

<section class="topic" id="topic-optimization" markdown="1">

## Numerical Optimization

In the field of legged robotics, I aim to address a key research challenge in the use of numerical optimization for trajectory planning. This research investigates methods to concurrently optimize both the sequence of contacts and their duration within a Model Predictive Control (MPC) framework.

Legged robots exhibit hybrid dynamics, and optimization of contact sequences is typically handled using Mixed-Integer approaches, which often suffer from high computational demands. My goal is to investigate parallel optimization techniques to enable real-time computation and deployment on physical robotic platforms.

</section>

<section class="topic" id="topic-construction" markdown="1">

## Robotics Applied to Construction

I collaborate as a scientific advisor with the robotics company **Address Robotics**, operating in the field of automated construction. Their goal is to employ legged robots and automated cranes for the autonomous assembly of prefabricated elements, enabling continuous progress monitoring while minimizing costly rework operations.

This research proposes a framework to automate a large number of construction-site processes by leveraging:

1. Heavy-duty legged robots capable of navigating challenging construction environments  
2. Automated cranes  
3. AI-driven navigation, coordination, and cooperation strategies

</section>

<section class="topic" id="topic-platforms" markdown="1">

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

</section>

You can check more about these in my Youtube Research [playlist](https://youtube.com/playlist?list=PLpppns-JGSyKlxNhpuYCevkTBI8-Apn-H&feature=shared)

</div>

<div class="research-panel" id="research-journals" markdown="1">

# Publications (Journals)

<p class="bib-all">All references in one file: <a href="{{ '/assets/data/publications.bib' | relative_url }}" download>publications.bib</a></p>

### 2025
- **Pseudo-Kinematic Trajectory Control and Planning of Tracked Vehicles**. *Robotics and Autonomous Systems*, 2025. [PDF](https://www.sciencedirect.com/science/article/pii/S0921889025003793) [Video](https://www.youtube.com/watch?v=TyeZ0vRkI04) <button type="button" class="bib-btn" data-bib="focchi26ras">BibTeX</button>
- **Smooth Human-Robot Shared Control for Autonomous Orchard Monitoring with UGVs**. *IEEE Transactions on Automation Science and Engineering*, 2025. [PDF](https://iit-dlslab.github.io/papers/elbou25tase.pdf) [Video](https://www.youtube.com/watch?v=OfC-wzxXLpg) <button type="button" class="bib-btn" data-bib="elbou25tase">BibTeX</button>
- **ALPINE: a Climbing Robot for Operations in Mountain Environments**. *Robotics and Autonomous Systems*, 2025. [PDF](https://www.sciencedirect.com/science/article/pii/S0921889025000855) [Video](https://www.youtube.com/watch?v=FqsREaoe-28) <button type="button" class="bib-btn" data-bib="focchi25ras">BibTeX</button>

### 2024
- **Efficient Reinforcement Learning for 3D Jumping Monopods**. *Sensors*, 2024. [PDF](https://pmc.ncbi.nlm.nih.gov/articles/PMC11314636/pdf/sensors-24-04981.pdf) <button type="button" class="bib-btn" data-bib="bussola24sensors">BibTeX</button>

### 2023
- **Reactive Landing Controller for Quadruped Robots**. *IEEE Robotics and Automation Letters*, 2023. [PDF](https://iit-dlslab.github.io/papers/roscia23ral.pdf) [Video](https://www.youtube.com/watch?v=wiuedeHfSEY) <button type="button" class="bib-btn" data-bib="roscia23ral">BibTeX</button>
- **An Efficient Paradigm for Feasibility Guarantees in Legged Locomotion**. *IEEE Transactions on Robotics*, 2023. [PDF](https://arxiv.org/pdf/2011.07967v2) <button type="button" class="bib-btn" data-bib="abdalla23tro">BibTeX</button>
- **Orientation Control System: Enhancing Aerial Maneuvers for Quadruped Robots**. *Sensors*, 2023. [PDF](https://www.mdpi.com/1424-8220/23/3/1234) [Video](https://www.youtube.com/watch?v=Zad20mtFJm0) <button type="button" class="bib-btn" data-bib="roscia23sensors">BibTeX</button>
- **Optimization-Based Reference Generator for Nonlinear Model Predictive Control of Legged Robots**. *Robotics*, 2023. [PDF](https://www.mdpi.com/2218-6581/12/1/6) <button type="button" class="bib-btn" data-bib="bratta23mdpi">BibTeX</button>

### 2021
- **Model Predictive Control with Environment Adaptation for Legged Locomotion**. *IEEE Access*, 2021. [PDF](https://doi.org/10.1109/ACCESS.2021.3118957) [Video](https://www.youtube.com/watch?v=r0-KIiw0eWM) <button type="button" class="bib-btn" data-bib="rathod21access">BibTeX</button>

### 2020
- **A simple yet effective whole-body locomotion framework for quadruped robots**. *Frontiers in Robotics and AI*, 2020. [PDF](https://hal.science/hal-03005133v2/file/Frontiers20_QuadrupedalWalking.pdf) [Video](https://www.youtube.com/watch?v=O6TSUHiwSlU) <button type="button" class="bib-btn" data-bib="raiola20frontiers">BibTeX</button>
- **Feasible Region: an Actuation-Aware Extension of the Support Region**. *IEEE Transactions on Robotics*, 2020. [PDF](https://iit-dlslab.github.io/papers/orsolino20tro.pdf) [Video](https://www.youtube.com/watch?v=9pvWO2Qmo9k) <button type="button" class="bib-btn" data-bib="orsolino20tro">BibTeX</button>
- **STANCE: Locomotion Adaptation over Soft Terrain**. *IEEE Transactions on Robotics*, 2020. [PDF](https://iit-dlslab.github.io/papers/fahmi19tro.pdf) [Video](https://www.youtube.com/watch?v=0BI4581DFjY) <button type="button" class="bib-btn" data-bib="fahmi20tro">BibTeX</button>
- **Heuristic Planning for Rough Terrain Locomotion in Presence of External Disturbances and Variable Perception Quality**. *Springer Tracts in Advanced Robotics*, 2020. [PDF](https://iit-dlslab.github.io/papers/focchi19star.pdf) [Video](https://www.youtube.com/watch?v=_7ud4zIt-Gw) [Video 2](https://www.youtube.com/watch?v=MWTmqse0ntg) <button type="button" class="bib-btn" data-bib="focchi2020star">BibTeX</button>
- **Motion Planning for Quadrupedal Locomotion: Coupled Planning, Terrain Mapping and Whole-Body Control**. *IEEE Transactions on Robotics*, 2020. [PDF](https://cmastalli.github.io/publications/locomotion20tro.pdf) <button type="button" class="bib-btn" data-bib="mastalli20tro">BibTeX</button>
- **Editorial: Bridging the Gap Between the Lab and the Real World: Future Perspectives for Legged Robots**. *Frontiers in Robotics and AI*, 2020. [PDF](https://www.frontiersin.org/articles/10.3389/frobt.2020.629002/full) <button type="button" class="bib-btn" data-bib="focchi20frontiers">BibTeX</button>

### 2019
- **Fast and Continuous Foothold Adaptation for Dynamic Locomotion through CNNs**. *IEEE Robotics and Automation Letters*, 2019. [PDF](https://iit-dlslab.github.io/papers/villarreal19ral.pdf) [Video](https://www.youtube.com/watch?v=rxn79dPnaCI) <button type="button" class="bib-btn" data-bib="villarreal19ral">BibTeX</button>
- **Passive Whole-Body Control for Quadruped Robots: Experimental Validation over Challenging Terrain**. *IEEE Robotics and Automation Letters*, 2019. [PDF](https://iit-dlslab.github.io/papers/fahmi19ral.pdf) [Video](https://www.youtube.com/watch?v=Lg3V_juoE1w) <button type="button" class="bib-btn" data-bib="fahmi2019ral">BibTeX</button>

### 2018
- **Simultaneous Contact, Gait, and Motion Planning for Robust Multi-Legged Locomotion via Mixed-Integer Convex Optimization**. *IEEE Robotics and Automation Letters*, 2018. [PDF](https://iit-dlslab.github.io/papers/aceituno_mastalli17ral.pdf) [Video](https://www.youtube.com/watch?v=s4PMXpbwUes) [Video 2](https://www.youtube.com/watch?v=RXIAQJx5938) <button type="button" class="bib-btn" data-bib="aceituno_mastalli17ral">BibTeX</button>
- **Application of Wrench-Based Feasibility Analysis to the Online Trajectory Optimization of Legged Robots**. *IEEE Robotics and Automation Letters*, 2018. [PDF](https://iit-dlslab.github.io/papers/orsolino18ral.pdf) <button type="button" class="bib-btn" data-bib="orsolino18ral">BibTeX</button>

### 2017
- **High-slope Terrain Locomotion for Torque-Controlled Quadruped Robots**. *Autonomous Robots*, 2017. [PDF](https://ihavoutis.github.io/publications/2016/auro2016focchi.pdf) [Video](https://www.youtube.com/watch?v=-qQp2RwQ-PQ) <button type="button" class="bib-btn" data-bib="focchi2016">BibTeX</button>

### 2016
- **Robot Impedance Control and Passivity Analysis with Inner Torque and Velocity Feedback Loops**. *Control Theory and Technology*, 2016. [PDF](https://iit-dlslab.github.io/papers/focchi16ctt.pdf) <button type="button" class="bib-btn" data-bib="focchi16ctt">BibTeX</button>
- **Design of the Hydraulically-Actuated, Torque-Controlled Quadruped Robot HyQ2Max**. *IEEE/ASME Transactions on Mechatronics*, 2016. [PDF](https://iit-dlslab.github.io/papers/tmech16semini.pdf) <button type="button" class="bib-btn" data-bib="tmech16semini">BibTeX</button>

### 2015
- **Towards Versatile Legged Robots through Active Impedance Control**. *The International Journal of Robotics Research*, 2015. [PDF](https://iit-dlslab.github.io/papers/semini15ijrr.pdf) [Video](https://www.youtube.com/watch?v=cNZPRsrwumQ) [Video 2](https://www.youtube.com/watch?v=ENHvCGrnr2g) <button type="button" class="bib-btn" data-bib="semini15ijrr">BibTeX</button>
- **On the Use of Positive Feedback for Improved Torque Control**. *Control Theory and Technology*, 2015. [PDF](https://iit-dlslab.github.io/papers/dallali15ctt.pdf) <button type="button" class="bib-btn" data-bib="dallali15ctt">BibTeX</button>

### 2014
- **Quadruped Robot Trotting over Irregular Terrain Assisted by Stereo-Vision**. *Intelligent Service Robotics*, 2014. [PDF](https://iit-dlslab.github.io/papers/bazeille14isr.pdf) <button type="button" class="bib-btn" data-bib="bazeille14isr">BibTeX</button>
- **Magnetorheologically Damped Compliant Foot for Legged Robotic Application**. *Journal of Mechanical Design*, 2014. [PDF](https://iit-dlslab.github.io/papers/kostamo14.pdf) [Video](https://www.youtube.com/watch?v=e5m1SmGV_ao) <button type="button" class="bib-btn" data-bib="kostamo14">BibTeX</button>

### 2011
- **Design of HyQ – a Hydraulically and Electrically Actuated Quadruped Robot**. *Journal of Systems and Control Engineering*, 2011. [PDF](https://iit-dlslab.github.io/papers/semini11jsce.pdf) <button type="button" class="bib-btn" data-bib="semini11hyqdesignjsce">BibTeX</button>

</div>

<div class="research-panel" id="research-conferences" markdown="1">

# Publications (Conferences)

<p class="bib-all">All references in one file: <a href="{{ '/assets/data/publications.bib' | relative_url }}" download>publications.bib</a></p>

### 2026
- **Cooperative and Optimization-based Framework for Aerial Manipulation**. *17th World Congress on Computational Mechanics & 10th European Congress on Computational Methods in Applied Sciences and Engineering (WCCM-ECCOMAS)*, 2026. [PDF](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/papers/eccomas26.pdf) <button type="button" class="bib-btn" data-bib="focchi26eccomas">BibTeX</button>
- **Bi-Level Optimization for Contact and Motion Planning in Rope-Assisted Legged Robots**. *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2026. [PDF](https://arxiv.org/abs/2604.26910) <button type="button" class="bib-btn" data-bib="malacarne26iros">BibTeX</button>

### 2024
- **Distributed Robot Perception for Tracked Vehicles**. *Italian Conference on Robotics and Intelligent Machines (I-RIM)*, 2024. [PDF](https://iit-dlslab.github.io/papers/bussola24irim.pdf) <button type="button" class="bib-btn" data-bib="bussola24irim">BibTeX</button>
- **ContactNet: Online Multi-Contact Planning for Acyclic Legged Robot Locomotion**. *Ubiquitous Robots*, 2024. [PDF](https://iit-dlslab.github.io/papers/bratta24ur.pdf) [Video](https://www.youtube.com/watch?v=ta1JpSigRKo) <button type="button" class="bib-btn" data-bib="bratta24ur">BibTeX</button>

### 2023
- **Locosim: An Open-Source Cross-Platform Robotics Framework**. *CLAWAR*, 2023. [Publisher](https://iit-dlslab.github.io/papers/focchi23clawar.pdf) [Video](https://www.youtube.com/watch?v=ZwV1LEqK-LU) [Video 2](https://www.youtube.com/watch?v=tW5CuDmQTII) <button type="button" class="bib-btn" data-bib="focchi23clawar">BibTeX</button>
- **CLIO: a Novel Robotic Solution for Exploration and Rescue Missions in Hostile Mountain Environments**. *ICRA*, 2023. [PDF](https://arxiv.org/abs/2209.09693) <button type="button" class="bib-btn" data-bib="focchi23icra">BibTeX</button>

### 2022
- **Towards a Generic Navigation and Locomotion Control System for Legged Space Exploration**. *ASTRA*, 2022. [PDF](https://iit-dlslab.github.io/papers/dettmann22astra.pdf) <button type="button" class="bib-btn" data-bib="dettmann22astra">BibTeX</button>
- **Foothold Evaluation Criterion for Dynamic Transition Feasibility for Quadruped Robots**. *ICRA*, 2022. [PDF](https://iit-dlslab.github.io/papers/clemente22icra.pdf) [Video](https://www.youtube.com/watch?v=2rBopUquyrc) <button type="button" class="bib-btn" data-bib="clemente22icra">BibTeX</button>

### 2020
- **On the Hardware Feasibility of Nonlinear Trajectory Optimization for Legged Locomotion based on a Simplified Dynamics**. *ICRA*, 2020. [PDF](https://iit-dlslab.github.io/papers/bratta20icra.pdf) [Video](https://www.youtube.com/watch?v=bpjlRvtVwe8) <button type="button" class="bib-btn" data-bib="bratta20icra">BibTeX</button>

### 2019
- **Brief Introduction to the Quadruped Robot HyQReal**. *I-RIM*, 2019. [PDF](https://iit-dlslab.github.io/papers/semini19irim.pdf) [Video](https://www.youtube.com/watch?v=pLsNs1ZS_TI) <button type="button" class="bib-btn" data-bib="Semini2019">BibTeX</button>
- **On the Detection and Localization of Shin Collisions and Reactive Actions in Quadruped Robots**. *CLAWAR*, 2019. [PDF](https://iit-dlslab.github.io/papers/barasuol19clawar.pdf) [Video](https://www.youtube.com/watch?v=vHc5ZpkCy8Y) <button type="button" class="bib-btn" data-bib="barasuol19clawar">BibTeX</button>

### 2017
- **Online Payload Identification for Quadruped Robots**. *IROS*, 2017. [PDF](https://iit-dlslab.github.io/papers/tournois17iros.pdf) [Video](https://www.youtube.com/watch?v=EDsBPYudHik) [Video 2](https://www.youtube.com/watch?v=2Pnj5hJVeJM) [Video 3](https://www.youtube.com/watch?v=3zZE9YTGRjw) <button type="button" class="bib-btn" data-bib="tournois17iros">BibTeX</button>
- **A Combined Limit Cycle-Zero Moment Point Based Approach for Omni-Directional Quadrupedal Bounding**. *CLAWAR*, 2017. [PDF](https://iit-dlslab.github.io/papers/orsolino17clawar.pdf) [Video](https://www.youtube.com/watch?v=005BMWixqsQ) <button type="button" class="bib-btn" data-bib="orsolino17clawar">BibTeX</button>
- **Validation of Computer Simulations of the HyQ Robot**. *CLAWAR*, 2017. [PDF](https://iit-dlslab.github.io/papers/frigerio17clawar.pdf) <button type="button" class="bib-btn" data-bib="frigerio17clawar">BibTeX</button>
- **Heterogeneous Sensor Fusion for Accurate State Estimation of Dynamic Legged Robots**. *Robotics: Science and Systems (RSS)*, 2017. [PDF](https://iit-dlslab.github.io/papers/nobili_camurri2017rss.pdf) <button type="button" class="bib-btn" data-bib="nobili_camurri2017rss">BibTeX</button>
- **Viscosity-based Height Reflex for Workspace Augmentation for Quadrupedal Locomotion on Rough Terrain**. *IROS*, 2017. [PDF](https://iit-dlslab.github.io/papers/focchi17iros.pdf) [Video](https://www.youtube.com/watch?v=FPkvu29WLUc) [Video 2](https://www.youtube.com/watch?v=pQPO5exJQd0) [Video 3](https://www.youtube.com/watch?v=vD5PTUf6rLQ) <button type="button" class="bib-btn" data-bib="focchi17iros">BibTeX</button>
- **Trajectory and Foothold Optimization using Low-Dimensional Models for Rough Terrain Locomotion**. *ICRA*, 2017. [PDF](https://iit-dlslab.github.io/papers/mastalli17icra.pdf) [Video](https://www.youtube.com/watch?v=79bb2KTULrw) <button type="button" class="bib-btn" data-bib="mastalli17icra">BibTeX</button>

### 2016
- **Towards a Multi-Legged Mobile Manipulator**. *ICRA*, 2016. [PDF](https://iit-dlslab.github.io/papers/icra16brehman.pdf) [Video](https://www.youtube.com/watch?v=RKwWxEc-ric) <button type="button" class="bib-btn" data-bib="icra16brehman">BibTeX</button>
- **A Design Method of a Robust Controller for Hydraulic Actuation with Disturbance Observers**. *AMC*, 2016. [PDF](https://iit-dlslab.github.io/papers/kuwahara16acm.pdf) <button type="button" class="bib-btn" data-bib="kuwahara16acm">BibTeX</button>
- **Hierarchical Planning of Dynamic Movements without Scheduled Contact Sequences**. *ICRA*, 2016. [PDF](https://iit-dlslab.github.io/papers/icra16mastalli.pdf) <button type="button" class="bib-btn" data-bib="icra16mastalli">BibTeX</button>

### 2015
- **Slip Detection and Recovery for Quadruped Robots**. *ISRR*, 2015. [PDF](https://iit-dlslab.github.io/papers/focchi15isrr.pdf) [Video](https://www.youtube.com/watch?v=cNZPRsrwumQ) [Video 2](https://www.youtube.com/watch?v=Hrwi9-411AM) <button type="button" class="bib-btn" data-bib="focchi15isrr">BibTeX</button>
- **Design of a Hydraulically Actuated Arm for a Quadruped Robot**. *CLAWAR*, 2015. [PDF](https://iit-dlslab.github.io/papers/rehman15clawar.pdf) [Video](https://www.youtube.com/watch?v=JhbHPZc-NGU) <button type="button" class="bib-btn" data-bib="rehman15clawar">BibTeX</button>
- **Planning and Execution of Dynamic Whole-Body Locomotion for a Hydraulic Quadruped on Challenging Terrain**. *ICRA*, 2015. [PDF](https://iit-dlslab.github.io/papers/winkler15icra.pdf) [Video](https://www.youtube.com/watch?v=MF-qxA_syZg) <button type="button" class="bib-btn" data-bib="winkler15icra">BibTeX</button>
- **Design Overview of the Hydraulic Quadruped Robots HyQ2Max and HyQ2Centaur**. *14th Scandinavian International Conference on Fluid Power (SICFP)*, 2015. [PDF](https://iit-dlslab.github.io/papers/semini15sicfp.pdf) [Video](https://www.youtube.com/watch?v=ENHvCGrnr2g) [Video 2](https://www.youtube.com/watch?v=2jvLalY6ubc) <button type="button" class="bib-btn" data-bib="semini15sicfp">BibTeX</button>

### 2014
- **Path Planning with Force-Based Foothold Adaptation and Virtual Model Control for Torque Controlled Quadruped Robots**. *ICRA*, 2014. [PDF](https://iit-dlslab.github.io/papers/winkler14icra.pdf) <button type="button" class="bib-btn" data-bib="winkler14icra">BibTeX</button>

### 2013
- **Local Reflex Generation for Obstacle Negotiation in Quadrupedal Locomotion**. *CLAWAR*, 2013. [PDF](https://iit-dlslab.github.io/papers/focchi13clawar.pdf) [Video](https://www.youtube.com/watch?v=_9H8EIs-hMc) <button type="button" class="bib-btn" data-bib="focchi2013a">BibTeX</button>
- **Vision Enhanced Reactive Locomotion Control for Trotting on Rough Terrain**. *TePRA*, 2013. [PDF](https://iit-dlslab.github.io/papers/bazeille13tepra.pdf) <button type="button" class="bib-btn" data-bib="bazeille13tepra">BibTeX</button>

### 2012
- **On the Role of Load Motion Compensation in High-Performance Force Control**. *IROS*, 2012. [PDF](https://iit-dlslab.github.io/papers/boaventura12iros.pdf) <button type="button" class="bib-btn" data-bib="boaventura12iros">BibTeX</button>
- **Design and Scaling of Versatile Quadruped Robots**. *CLAWAR*, 2012. [PDF](https://iit-dlslab.github.io/papers/semini12clawar.pdf) [Video](https://www.youtube.com/watch?v=wPxXwYGZmd8) <button type="button" class="bib-btn" data-bib="semini12clawar">BibTeX</button>
- **Dynamic Torque Control of a Hydraulic Quadruped Robot**. *ICRA*, 2012. [PDF](https://iit-dlslab.github.io/papers/boaventura12icra.pdf) <button type="button" class="bib-btn" data-bib="boaventura12icra">BibTeX</button>
- **Torque-Control Based Compliant Actuation of a Quadruped Robot**. *AMC*, 2012. [PDF](https://iit-dlslab.github.io/papers/focchi12acm.pdf) <button type="button" class="bib-btn" data-bib="focchi12acm">BibTeX</button>

### 2011
- **Novel Concept for an Air-Pressure Driven Micro-Turbine for Power Generation**. *ASME Turbo Expo*, 2011. [PDF](https://www.researchgate.net/publication/261360745_Novel_Concept_for_an_Air-Pressure_Driven_Micro-Turbine_for_Power_Generation) [Video](https://www.youtube.com/watch?v=q9NsmhQHHFE) <button type="button" class="bib-btn" data-bib="focchi11turboexpo">BibTeX</button>

### 2010
- **Control of a Hydraulically-Actuated Quadruped Robot Leg**. *ICRA*, 2010. [PDF](https://iit-dlslab.github.io/papers/icra10focchi.pdf) <button type="button" class="bib-btn" data-bib="focchi10icra">BibTeX</button>
- **Water/Air Performance Analysis of a Fluidic Muscle**. *IROS*, 2010. [PDF](https://ieeexplore.ieee.org/document/5650432) <button type="button" class="bib-btn" data-bib="focchi10iros">BibTeX</button>

</div>

>   A brief presentation of my research work can be found  [here](https://github.com/mfocchi/mfocchi.github.io/blob/master/_data/ResearchPresentation.pdf)   

>  The video of my talk  for "PI stories" collection of seminars   at University of Trento can be found [here](https://www.youtube.com/watch?v=cxCF_FkHoKU)   

>   The video of my talk at Acquario di Genova on my recent research results can be found  [here](https://youtu.be/UBjLsTrt-54)

>   The video of my talk at the ICRA workshop on Opportunities and Challenges in Space Robotics ([video](https://youtu.be/LYoq4_mGvCQ))

>   The video of my talk at the University of Porto  ([video](https://youtu.be/70j4qgd30GI))

<script>
(function () {
  var bar = document.getElementById('research-tabbar');
  var panels = document.querySelectorAll('.research-panel');
  if (!bar || !panels.length) { return; }
  document.documentElement.classList.add('research-js');
  bar.hidden = false;

  var topicsPanel = document.getElementById('research-topics');
  var tbar = document.getElementById('topic-tabbar');
  var topics = topicsPanel ? topicsPanel.querySelectorAll('.topic') : [];
  if (tbar) { tbar.hidden = false; }
  function showTopic(key) {
    var found = false;
    for (var i = 0; i < topics.length; i++) {
      var on = topics[i].id === 'topic-' + key;
      topics[i].classList.toggle('on', on);
      found = found || on;
    }
    if (!found) { key = 'all'; }
    topicsPanel.classList.toggle('topic-filtered', key !== 'all');
    var tb = tbar ? tbar.querySelectorAll('button') : [];
    for (var j = 0; j < tb.length; j++) {
      tb[j].setAttribute('aria-pressed', tb[j].getAttribute('data-topic') === key ? 'true' : 'false');
    }
    return key;
  }

  function show(key, push) {
    var sub = null;
    if (key.indexOf('topics-') === 0) { sub = key.slice(7); key = 'topics'; }
    var found = false;
    for (var i = 0; i < panels.length; i++) {
      var on = panels[i].id === 'research-' + key;
      panels[i].classList.toggle('active', on);
      found = found || on;
    }
    if (!found) { return show(panels[0].id.replace('research-', ''), false); }
    var btns = bar.querySelectorAll('button');
    for (var j = 0; j < btns.length; j++) {
      btns[j].setAttribute('aria-selected', btns[j].getAttribute('data-tab') === key ? 'true' : 'false');
    }
    var hash = key;
    if (key === 'topics' && topicsPanel) {
      sub = showTopic(sub || 'all');
      if (sub !== 'all') { hash = 'topics-' + sub; }
    }
    if (push && history.replaceState) { history.replaceState(null, '', '#' + hash); }
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (b) { show(b.getAttribute('data-tab'), true); }
  });
  if (tbar) {
    tbar.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) { return; }
      var t = b.getAttribute('data-topic');
      show(t === 'all' ? 'topics' : 'topics-' + t, true);
    });
  }
  show(location.hash.replace('#', '') || panels[0].id.replace('research-', ''), false);
})();
</script>

<dialog id="bib-dialog" aria-labelledby="bib-dialog-title">
  <header><strong id="bib-dialog-title">BibTeX</strong><button type="button" id="bib-copy">Copy</button><button type="button" id="bib-close">Close</button></header>
  <pre><code id="bib-code"></code></pre>
</dialog>

<script>
(function () {
  var dlg = document.getElementById('bib-dialog');
  var code = document.getElementById('bib-code');
  var copyBtn = document.getElementById('bib-copy');
  var url = "{{ '/assets/data/publications.bib' | relative_url }}";
  var entries = null;
  function load() {
    if (entries) { return Promise.resolve(entries); }
    return fetch(url).then(function (r) { return r.text(); }).then(function (txt) {
      entries = {};
      txt.split(/\n(?=@)/).forEach(function (chunk) {
        var m = chunk.match(/^@\w+\{([^,\s]+),/);
        if (m) { entries[m[1]] = chunk.trim(); }
      });
      return entries;
    });
  }
  function open(key, title) {
    document.getElementById('bib-dialog-title').textContent = title || key;
    code.textContent = 'Loading…';
    copyBtn.textContent = 'Copy';
    if (dlg.showModal) { dlg.showModal(); } else { dlg.setAttribute('open', ''); }
    load().then(function (e) {
      code.textContent = e[key] || 'No BibTeX entry found for ' + key + '.';
    }).catch(function () {
      code.textContent = 'Could not load the BibTeX file. Download it from ' + url;
    });
  }
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest('.bib-btn');
    if (!b) { return; }
    var li = b.closest('li'); var strong = li && li.querySelector('strong');
    open(b.getAttribute('data-bib'), strong ? strong.textContent : '');
  });
  document.getElementById('bib-close').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (ev) { if (ev.target === dlg) { dlg.close(); } });
  copyBtn.addEventListener('click', function () {
    var t = code.textContent;
    var done = function () { copyBtn.textContent = 'Copied'; };
    if (navigator.clipboard) { navigator.clipboard.writeText(t).then(done); }
    else { var r = document.createRange(); r.selectNodeContents(code); var sel = getSelection();
      sel.removeAllRanges(); sel.addRange(r); document.execCommand('copy'); done(); }
  });
})();
</script>
