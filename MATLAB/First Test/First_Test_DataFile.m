% Simscape(TM) Multibody(TM) version: 7.2

% This is a model data file derived from a Simscape Multibody Import XML file using the smimport function.
% The data in this file sets the block parameter values in an imported Simscape Multibody model.
% For more information on this file, see the smimport function help page in the Simscape Multibody documentation.
% You can modify numerical values, but avoid any other changes to this file.
% Do not add code to this file. Do not edit the physical units shown in comments.

%%%VariableName:smiData


%============= RigidTransform =============%

%Initialize the RigidTransform structure array by filling in null values.
smiData.RigidTransform(4).translation = [0.0 0.0 0.0];
smiData.RigidTransform(4).angle = 0.0;
smiData.RigidTransform(4).axis = [0.0 0.0 0.0];
smiData.RigidTransform(4).ID = '';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(1).translation = [0 0 0];  % cm
smiData.RigidTransform(1).angle = 2.0943951023931953;  % rad
smiData.RigidTransform(1).axis = [-0.57735026918962584 -0.57735026918962584 0.57735026918962584];
smiData.RigidTransform(1).ID = 'B[spur gear_am-3:-:]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(2).translation = [0 0 0];  % cm
smiData.RigidTransform(2).angle = 0;  % rad
smiData.RigidTransform(2).axis = [0 0 0];
smiData.RigidTransform(2).ID = 'F[spur gear_am-3:-:]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(3).translation = [0 0 0];  % cm
smiData.RigidTransform(3).angle = 2.0943951023931953;  % rad
smiData.RigidTransform(3).axis = [-0.57735026918962584 -0.57735026918962584 0.57735026918962584];
smiData.RigidTransform(3).ID = 'B[spur gear_am-4:-:]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(4).translation = [7.9999999999999991 0 0];  % cm
smiData.RigidTransform(4).angle = 1.7772239894833365e-16;  % rad
smiData.RigidTransform(4).axis = [-0.016376977170602987 0.99986588831640499 -1.4550826653802591e-18];
smiData.RigidTransform(4).ID = 'F[spur gear_am-4:-:]';


%============= Solid =============%
%Center of Mass (CoM) %Moments of Inertia (MoI) %Product of Inertia (PoI)

%Initialize the Solid structure array by filling in null values.
smiData.Solid(2).mass = 0.0;
smiData.Solid(2).CoM = [0.0 0.0 0.0];
smiData.Solid(2).MoI = [0.0 0.0 0.0];
smiData.Solid(2).PoI = [0.0 0.0 0.0];
smiData.Solid(2).color = [0.0 0.0 0.0];
smiData.Solid(2).opacity = 0.0;
smiData.Solid(2).ID = '';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(1).mass = 0.013916940878568301;  % kg
smiData.Solid(1).CoM = [5.0000000000000009 -0.14408338854756844 0];  % mm
smiData.Solid(1).MoI = [4.8413795272202318 2.5479474022039841 2.5253811396590513];  % kg*mm^2
smiData.Solid(1).PoI = [0 0 0];  % kg*mm^2
smiData.Solid(1).color = [0.77647058823529413 0.75686274509803919 0.73725490196078436];
smiData.Solid(1).opacity = 1;
smiData.Solid(1).ID = 'spur gear_am*:*Metric - Spur gear 3M 16T 14.5PA 10FW ---S16N75H50L20S1';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(2).mass = 0.082403103230141037;  % kg
smiData.Solid(2).CoM = [4.9999999999999991 -0.071734757975770516 0];  % mm
smiData.Solid(2).MoI = [129.03777831901053 65.253169702399148 65.157993670447055];  % kg*mm^2
smiData.Solid(2).PoI = [0 0 0];  % kg*mm^2
smiData.Solid(2).color = [0.77647058823529413 0.75686274509803919 0.73725490196078436];
smiData.Solid(2).opacity = 1;
smiData.Solid(2).ID = 'spur gear_am*:*Metric - Spur gear 3M 36T 14.5PA 10FW ---S36N75H50L30R1';


%============= Joint =============%
%X Revolute Primitive (Rx) %Y Revolute Primitive (Ry) %Z Revolute Primitive (Rz)
%X Prismatic Primitive (Px) %Y Prismatic Primitive (Py) %Z Prismatic Primitive (Pz) %Spherical Primitive (S)
%Constant Velocity Primitive (CV) %Lead Screw Primitive (LS)
%Position Target (Pos)

%Initialize the RevoluteJoint structure array by filling in null values.
smiData.RevoluteJoint(2).Rz.Pos = 0.0;
smiData.RevoluteJoint(2).ID = '';

smiData.RevoluteJoint(1).Rz.Pos = -38.51412799979029;  % deg
smiData.RevoluteJoint(1).ID = '[spur gear_am-3:-:]';

smiData.RevoluteJoint(2).Rz.Pos = -104.55713073659615;  % deg
smiData.RevoluteJoint(2).ID = '[spur gear_am-4:-:]';

