### **Syllabus** Introduction To Ro

### botics

#### **Introduction**

**- Introduction to robotics**: What is a robot? Robots History. Robot classification. Evolution toward Industrial robots. Other kind of robots: service robots, exoskeletons. Under-actuated robots: underwater robots, space robots, drones, legged robots, humanoids, quadrupeds.

\- **Robot’s functional units:** Mechanical Structure: joints, links, end-effector, workspace, robot classification based on joint arrangement. Overview of functional units of a robot: sensors, actuators, etc. Overview of the main robotics topics: control, perception, estimation, planning.



#### **Sensors**

**- Introduction to measurement:** properties of a measurement system (accuracy, repeatability, uncertainty), sensors characteristics (sensitivity, range, resolution, dynamic response), type of measurements errors (systematic, random). Non idealities in sensors: non-linearity, offset, scaling, dead-band, hysteresis.

**- Proprioceptive sensors:** Types of (propio-ceptive) sensors. Position sensors (potentiometers, relative/absolute encoders) quantization noise, contact switches, LDR, inertial sensors (accelerometers, gyros).

**- Exteroceptive sensors:** Types of extero-ceptive sensors. Force sensors (strain gauges, reading/mounting of strain gauges, wheatstone bridge, F/T 6 axis force sensors). Vision sensors. Passive cameras, stereo camera, triangulation in stereo-vision. Camera modeling (pinhole model), camera calibration. Active sensors: LiDAR, Structured light sensors, basic image processing, visual odometry, state estimation, point cloud. Proxy-sensors.

**- Signal processing:** Analog/discrete signals. Sampling, quantization and reconstruction (A/D, D/A converters). Problems in digital implementation: quantization errors, delays, aliasing (Nyquist theorem). Low-pass filter (discrete implementation). Basic signal processing: average, moving average, weighted average.



#### **Actuators**

**- Typer of actuators:** types of actuators in robotics:  pneumatic, hydraulic actuators, EHAs, electric motors, Series elastic actuators.

**- Electrical actuators:** Review of some useful notions of physics. Synchronous/ Asynchronous AC Motor, brushed/brushless DC Motor, efficiency, model of a DC motor steady state response. Motor control : voltage / current.

**- Transmissions**: types of transmissions, modeling transmission, gearbox,  Optimal choice of reduction ratio, modeling elasticity in transmission.

**- Non idealities:** Non idealities in actuators: modeling friction, back-lash, dead-band

**- Simulation of actuators:** Simulation of actuators: state space dynamics of a DC motor, discrete equivalent model, integration of dynamics, time responses.



#### **Control basics**

**- Introduction to control:** open loop control, feed-back concept, bang-bang controller, transient/steady-state response, static/dynamic control specifications, design of a controller.

**- PID:** P, PD, PID control, current control, anti-windup technique

**- Implementation of PID:**  realizability issue of PID, Digital PID, tuning techniques for PID.



#### **Kinematics:**

**- Kinematics of a rigid body** Position and orientation of a rigid body. Reference frames. Rotation matrices (properties, composition, and interpretations). Derivative of a rotation matrix. Minimal representations of orientation. Skew-symmetric matrices. Exponential maps and the Rodríguez formula. Euler angles. Relation between Euler rates and angular velocity. Unit quaternions.

\- **Manipulator direct kinematics:** Definition of forward and inverse kinematics. Joint, task and actuation spaces. Generalized coordinates. Forward kinematics of robot manipulators. Homogeneous transformations (properties, composition and interpretations). Inverse of a homogeneous transformation matrix. Frame placement. Direct kinematics of a kinematic chain.

**- Inverse Kinematics:** Definition of inverse kinematics. Solvability and workspace. Closed form (analytical) solutions. Examples.  

**- Direct Differential Kinematics:** Linear and angular velocity of a rigid body. Linear and velocity of a manipulator link driven from prismatic or revolute joints. Contribution of prismatic and revolute joints to end-effector velocity. The Geometric Jacobian. The Analytical Jacobian. Relationship between Geometric and Analytical Jacobian.

**- Numerical Inverse Kinematics:** Gauss-Newton iterative approach. Pathological cases . Line search. Discussion on multiple solutions.

**- Redundancy and Singularities:** Definition of redundancy. Redundant manipulators. Primer on linear algebra sub-spaces. Redundancy and vector null space. The pseudo-inverse. Geometric interpretation of inverse kinematics mapping. Singular values. Definition of singularity. Types of singularities. Inverse differential kinematics and singularities. Damped least-squares method. Higher order differential inversion. 



#### **Dynamics:**

**- Statics:** statics vs. dynamics. Principle of virtual works. Kineto-static duality and analysis of sub-spaces. Velocity and force transformations.

\- **Dynamic of a rigid body:** Kinetic energy of a rigid body. Examples of moments of inertia. Potential gravitational energy.  Euler-Lagrange method. Contribution of non consevative forces. Linearity of the model in the dynamic parameters. Analysis of inertial couplings, Coriolis and centrifugal effects. Recursive Newton-Euler method. Examples. 

**- Interaction dynamics:** Rigid and compliant contact models. Constrained robot dynamics. Simulation with a compliant contact model.

\- **Under-actuation:** Definition and examples of under-actuated robots. Modeling of floating base robots. Structure of the floating base dynamics. 



#### **Joint Space control** 

**-** **PID for manipulators:** Overview of control problems in robotics. The concept of stability. PD, PD + gravity compensation, PID control.

**- Inverse dynamics.** Decentralized vs. centralized control. Feedback linearization in robotics. Joint space Inverse dynamics (Computed torque).



#### **Task Space Control**

**- Cartesian space control:** inverse kinematics control, direct Cartesian space control. Cartesian PD, PD+ gravity compensation. Inverse dynamics in Cartesian space (non-redundant and redundant case). 

**- Orientation Control:** orientation control with different parametrization of orientation (rotation matrix, angle-axis, Euler angle, quaternions).

**- Interaction Control:** Applications. passive/ active methods. Direct force control. Cartesian space impedance control, concept of inertia shaping. Superimposition of impedances. Simplified formulations. Compliance control. Selection of impedance parameters. Torsional impedance. Admittance control. Visual servoing.

### **Lab sessions**

**- Lab Python: i**ntroductory lecture to python programming and to the usage of the *numpy* library

**- Lab Control:** simulation and control of a DC motor, PID design and tuning (Matlab).

**-** **Lab** **Kinematics/Dynamics:** learn to build a robot model using the Unified Robot Description Format (URDF), compute the direct/inverse kinematics of a 4-DoF serial manipulator. Design a reference trajectory with polynomials. Implement the numerical inverse kinematics.  Compute and analyze the forward/inverse dynamics of a 4-DoF serial manipulator using the Recursive Newton-Euler Algorithm (RNEA). 

**- Lab Joint Space Control:** design motion controllers (of increasing complexity) in the joint space for a manipulator in free-motion. Implement a centralized approach (i.e. inverse dynamics). Implement the interaction with the environment with a compliant contact model.

**-** **Lab** **Task Space Control:** design a motion controllers (of increasing complexity) in the task space for a manipulator in free-motion. Implement a centralized approach (i.e. inverse dynamics). Implement the control of the orientation using the angle-axis representation.

