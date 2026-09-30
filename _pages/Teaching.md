---
title: "Teaching"
permalink: /Teaching/
header:

---



# Legged robots summer school (WHERE)

#### **Department of Information Engineering and Computer Science (DISI),   University of Trento, (Trento, Italy)**

The lectures in this course are organized into three main areas: Modeling, Control, and Planning. Each area presents key results from the literature, with a particular focus on legged robots. The Control section provides a comprehensive overview of the most common control strategies for the dynamic control of robotic systems, with emphasis on legged robots (bipeds and quadrupeds). The topics include position, force, impedance, admittance control, and inverse dynamics. Cartesian-space control is presented together with its extension to floating-base systems (e.g., legged robots). The problem of ensuring locomotion stability is addressed both from a projection-based and an optimization-based perspective, including Convex Quadratic Programming formulations. In the Modeling section, a concise introduction to approximated models—such as the Linear Inverted Pendulum, Single Rigid Body Model, and Centroidal Dynamics—is provided, along with a discussion of their advantages and limitations. These models are later employed to plan feasible Center of Mass (CoM) trajectories for legged robots by solving optimal control problems in the Planning section. The Planning part also discusses different formulations of the direct optimal control problem, including single shooting, multiple shooting, and direct collocation. Model Predictive Control (MPC) strategies for real-time applications are presented, with a particular focus on feasibility and stability guarantees. Sample-based approaches to MPC are also briefly introduced. Finally, the course concludes with an introduction to State Estimation and Reinforcement Learning, highlighting algorithms capable of operating under weaker assumptions (e.g., limited model knowledge or imperfect sensing) compared to model-based methods. These approaches are shown to generate robust trajectories in real-world scenarios. Throughout the course, Python-based hands-on exercises will allow students to implement and test the concepts covered in the lectures on practical problems such as legged locomotion on flat terrain. The goal of the course is to enable students to design controllers and plan simple locomotion trajectories for robots in complex environments, while developing a critical understanding of the advantages and limitations of various state-of-the-art approaches. The course combines both theoretical foundations and practical implementation, relying on Python and open-source libraries for robot visualization, multi-body dynamics computation, and trajectory optimization. The final hours of each day will be dedicated to practical exercises. On Friday afternoon, the last two hours will feature a live session with the Go2 quadruped, during which participants will test the developed software.

- the recordings of the Lectures, the slides and the software for the practical sessions can be found [here](https://github.com/idra-lab/where_summer_school) 



# Fundamental of Robotics

#### **Department of Information Engineering and Computer Science (DISI),   University of Trento, (Trento, Italy)**

﻿The panorama of robotics has undergone a significant change in the last decade. Until the early years of this century, robots were seen as heavy and dangerous machines used to perform rigidly defined tasks within controlled and structured environments. Recent advances in artificial intelligence have had a profound impact on the types of activities a robot can perform and the level of safety and reliability with which these activities can be carried out. Modern robots assist the elderly or disabled, work side by side with human workers, and drive on highways with little or no assistance. This paradigm shift requires the robot to perceive and understand the surrounding environment, autonomously plan an appropriate course of action for a task, and ensure its correct execution, reacting appropriately to unforeseen events. To design a machine of this complexity, engineers need various skills that touch on different disciplines. Robots are physical machines created by humans, so their movement can be analyzed and controlled through appropriate mathematical models. Robots move in a partially known environment, so they must create a map of the surrounding environment, localize themselves within the environment, detect, classify, and recognize the different objects they interact with. Robots must be autonomous or semi-autonomous, so they need the ability to decide on a sequence of actions (a plan), implement it within appropriate safety limits, and adapt it to changes as needed. Finally, robots incorporate computer machines that need to be programmed using appropriate languages and frameworks. In this course bachelor students will be introduced to each of these different aspects and will have the opportunity to put them into practice using our advanced teaching laboratories and facilities. After completing the course, they will be able to pursue a career as robotic application developers and/or continue with advanced studies in the field of intelligent robots.

- the framework used for the LAB sessions is Locosim: https://github.com/mfocchi/locosim (check fdr_exercises folder)

  

# **Introduction To Robotics**

#### **Department of Information Engineering and Computer Science (DISI),   University of Trento, (Trento, Italy)**

﻿The course offers a bird-eye view on the most important topics related to modern robotics, highlighting the main problems that need to be faced in order to make the robots operate correctly in the environment. Specifically, the course will cover the following topics: taxonomy of the different types of robots, physical modelling of robots (direct and inverse kinematics and dynamics), simulation of models, sensing and actuation solutions for perception and action. Using the developed models, the most famous methodologies to control robot motion and interaction, will be presented. These methods will be first studied in theory, and then implemented in simulation (with the Python language) to gain practical experience. Attention will be also paid to illustrate the most common non idealities and issues that are present when controlling robots. The course will adopt a combination of simulation models and lab experiences to consolidate the knowledge transmitted during the theoretical lessons. After completing the course, students will be able to:

\- select the most suitable sensors and actuators for a given robotic application

\- model the kinematics and dynamics any kind of robot

\- understand the working principles of several control algorithms for robotic systems

\- choose the appropriate approach(es) to control a specific system for a given target application

\- implement, tune, and test control algorithms with the Python language

you can find videos and  slides of all the lectures of the first academic  year (20 /21)

You can also find [here](https://www.dropbox.com/sh/5trh0s5y1xzdjds/AACchznJb7606MbQKb6-fUiUa) a virtual machine (password:  student) containing the Python software needed for the lab sessions.

- the syllabus can be found  [here](https://github.com/mfocchi/mfocchi.github.io/blob/master/_pages/syllabus_introrob.md)

- the recordings of the Lectures are [here](https://youtu.be/kN7llbDnH_s?si=G9WStw_x5k5KUtHn) 

- the pdf of the slides are  [here](https://www.dropbox.com/sh/if2lq3s6c0zayxl/AADr7SYiQU1Zn96tLKv7NnXwa?dl=0)

- the framework used for the LAB sessions is Locosim: https://github.com/mfocchi/locosim (check introrob_exercises folder)

  



# Control of Legged Robots

#### **IIT/Dibris, University of Genova, 2020 (Genova, Italy)**

The course is meant to provide to post-graduate students a broad overview on the most common control strategies for fixed-based robots (position, force, impedance, admittance control and inverse dynamics).Modeling of actuators, gear-box, friction and contact models is also briefly discussed. Cartesian space control is presented as well as the extension to floating-base (e.g. legged) robots. The problem of ensuring locomotion stability for a legged robot is tackled both from a projection-based and an optimization-based perspective (Convex Quadratic Programming).  Python templates will be provided to the students to implement in practice what was presented in the theory. The goal of the course is to allow students to design controllers and  make them aware of pros and cons of the different state-of-the art approaches. 

### **Prerequisites:**

A basic knowledge on articulated body dynamics and kinematics is required such as can be obtained from a first course in dynamics at undergraduate level. A basic knowledge of linear systems and linear algebra is also required.

Interested people can find:

- the recordings of the Lectures  [here](https://www.youtube.com/playlist?list=PLpppns-JGSyKFwngvh-DYRBpH9NUdqH4J) 

- the pdf of the slides  [here](https://www.dropbox.com/sh/etxpgbsoxqgoyco/AAAXDiL7nLiHMLSftgZ4A1d5a ) 

- the framework used for the LAB sessions is Locosim: https://github.com/mfocchi/locosim 

  Note that the branch compatible with the video lectures is an old branch called   **controlOfLeggedRobots** 

