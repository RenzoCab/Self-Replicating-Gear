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
smiData.RigidTransform(1).translation = [0 0 1];  % cm
smiData.RigidTransform(1).angle = 3.1415926535897931;  % rad
smiData.RigidTransform(1).axis = [1 0 0];
smiData.RigidTransform(1).ID = 'B[Gear_1-3:-:]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(2).translation = [-13.506133243155627 13.49481011603576 0];  % cm
smiData.RigidTransform(2).angle = 3.1415926535897931;  % rad
smiData.RigidTransform(2).axis = [1 -1.9988711917800364e-32 -2.1722117397191391e-16];
smiData.RigidTransform(2).ID = 'F[Gear_1-3:-:]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(3).translation = [0 0 0.99999999999999967];  % cm
smiData.RigidTransform(3).angle = 3.1415926535897931;  % rad
smiData.RigidTransform(3).axis = [1 0 0];
smiData.RigidTransform(3).ID = 'B[Gear_1-4:-:]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(4).translation = [-25.506133243155627 13.49481011603576 -2.2204460492503131e-16];  % cm
smiData.RigidTransform(4).angle = 3.1415926535897931;  % rad
smiData.RigidTransform(4).axis = [-1 -7.1289622011827393e-34 5.9944550548187283e-17];
smiData.RigidTransform(4).ID = 'F[Gear_1-4:-:]';


%============= Solid =============%
%Center of Mass (CoM) %Moments of Inertia (MoI) %Product of Inertia (PoI)

%Initialize the Solid structure array by filling in null values.
smiData.Solid(1).mass = 0.0;
smiData.Solid(1).CoM = [0.0 0.0 0.0];
smiData.Solid(1).MoI = [0.0 0.0 0.0];
smiData.Solid(1).PoI = [0.0 0.0 0.0];
smiData.Solid(1).color = [0.0 0.0 0.0];
smiData.Solid(1).opacity = 0.0;
smiData.Solid(1).ID = '';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(1).mass = 9.9999999999999995e-07;  % kg
smiData.Solid(1).CoM = [0 0.0095571770803032242 0.49999999999999994];  % cm
smiData.Solid(1).MoI = [9.0698607534794626e-06 9.0913218487239262e-06 1.7994515935536723e-05];  % kg*cm^2
smiData.Solid(1).PoI = [0 0 0];  % kg*cm^2
smiData.Solid(1).color = [0.792156862745098 0.81960784313725488 0.93333333333333335];
smiData.Solid(1).opacity = 1;
smiData.Solid(1).ID = 'Gear_1*:*Default';


%============= Joint =============%
%X Revolute Primitive (Rx) %Y Revolute Primitive (Ry) %Z Revolute Primitive (Rz)
%X Prismatic Primitive (Px) %Y Prismatic Primitive (Py) %Z Prismatic Primitive (Pz) %Spherical Primitive (S)
%Constant Velocity Primitive (CV) %Lead Screw Primitive (LS)
%Position Target (Pos)

%Initialize the RevoluteJoint structure array by filling in null values.
smiData.RevoluteJoint(2).Rz.Pos = 0.0;
smiData.RevoluteJoint(2).ID = '';

smiData.RevoluteJoint(1).Rz.Pos = -27.788937002457672;  % deg
smiData.RevoluteJoint(1).ID = '[Gear_1-3:-:]';

smiData.RevoluteJoint(2).Rz.Pos = -22.442772096332245;  % deg
smiData.RevoluteJoint(2).ID = '[Gear_1-4:-:]';

