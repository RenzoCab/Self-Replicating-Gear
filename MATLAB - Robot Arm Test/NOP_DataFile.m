% Simscape(TM) Multibody(TM) version: 7.2

% This is a model data file derived from a Simscape Multibody Import XML file using the smimport function.
% The data in this file sets the block parameter values in an imported Simscape Multibody model.
% For more information on this file, see the smimport function help page in the Simscape Multibody documentation.
% You can modify numerical values, but avoid any other changes to this file.
% Do not add code to this file. Do not edit the physical units shown in comments.

%%%VariableName:smiData


%============= RigidTransform =============%

%Initialize the RigidTransform structure array by filling in null values.
smiData.RigidTransform(9).translation = [0.0 0.0 0.0];
smiData.RigidTransform(9).angle = 0.0;
smiData.RigidTransform(9).axis = [0.0 0.0 0.0];
smiData.RigidTransform(9).ID = '';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(1).translation = [0 0 -2.5000000000000022];  % mm
smiData.RigidTransform(1).angle = 3.1415926535897865;  % rad
smiData.RigidTransform(1).axis = [-1 -1.9381614862164639e-31 5.5511151231260859e-17];
smiData.RigidTransform(1).ID = 'B[link 1-1:-:link 2-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(2).translation = [-89.978102007914856 -1.9852352640399076 -2.4999999999372982];  % mm
smiData.RigidTransform(2).angle = 3.1415926535897447;  % rad
smiData.RigidTransform(2).axis = [1 -8.4292975874720724e-27 -3.4833898832217646e-13];
smiData.RigidTransform(2).ID = 'F[link 1-1:-:link 2-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(3).translation = [1.9845236565174673e-11 1.3877787807814457e-12 28.499999999999993];  % mm
smiData.RigidTransform(3).angle = 3.1415926535897452;  % rad
smiData.RigidTransform(3).axis = [1 -8.3429785739772034e-27 -3.4819819603045666e-13];
smiData.RigidTransform(3).ID = 'B[link 2-1:-:link 3-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(4).translation = [-108.00000000000009 -5.5422333389287814e-13 28.500000000000028];  % mm
smiData.RigidTransform(4).angle = 3.1415926535897865;  % rad
smiData.RigidTransform(4).axis = [1 -9.3439155885251244e-31 -2.6883497133354354e-16];
smiData.RigidTransform(4).ID = 'F[link 2-1:-:link 3-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(5).translation = [0 1.3877787807814457e-13 18.000000000000004];  % mm
smiData.RigidTransform(5).angle = 3.1415926535897865;  % rad
smiData.RigidTransform(5).axis = [1 0 0];
smiData.RigidTransform(5).ID = 'B[link 3-1:-:link 4-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(6).translation = [-62.5 6.0396132539608516e-14 17.968710604668079];  % mm
smiData.RigidTransform(6).angle = 3.1415926535897927;  % rad
smiData.RigidTransform(6).axis = [-1 -3.1853939649810305e-31 1.7484171077227738e-15];
smiData.RigidTransform(6).ID = 'F[link 3-1:-:link 4-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(7).translation = [0 -1.9203147363637235e-13 55];  % mm
smiData.RigidTransform(7).angle = 3.1415926535897896;  % rad
smiData.RigidTransform(7).axis = [-1 -0 -0];
smiData.RigidTransform(7).ID = 'B[de robot-1:-:link 1-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(8).translation = [50.000000000000092 90.000000000000085 6.6791017161449417e-13];  % mm
smiData.RigidTransform(8).angle = 2.0943951023931913;  % rad
smiData.RigidTransform(8).axis = [-0.5773502691896244 -0.5773502691896244 -0.57735026918962851];
smiData.RigidTransform(8).ID = 'F[de robot-1:-:link 1-1]';

%Translation Method - Cartesian
%Rotation Method - Arbitrary Axis
smiData.RigidTransform(9).translation = [0 0 0];  % mm
smiData.RigidTransform(9).angle = 0;  % rad
smiData.RigidTransform(9).axis = [0 0 0];
smiData.RigidTransform(9).ID = 'RootGround[de robot-1]';


%============= Solid =============%
%Center of Mass (CoM) %Moments of Inertia (MoI) %Product of Inertia (PoI)

%Initialize the Solid structure array by filling in null values.
smiData.Solid(5).mass = 0.0;
smiData.Solid(5).CoM = [0.0 0.0 0.0];
smiData.Solid(5).MoI = [0.0 0.0 0.0];
smiData.Solid(5).PoI = [0.0 0.0 0.0];
smiData.Solid(5).color = [0.0 0.0 0.0];
smiData.Solid(5).opacity = 0.0;
smiData.Solid(5).ID = '';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(1).mass = 0.012615620141849726;  % kg
smiData.Solid(1).CoM = [-40.539132618291042 0 0];  % mm
smiData.Solid(1).MoI = [0.65519102287236575 2.209743937358247 2.2119733021349095];  % kg*mm^2
smiData.Solid(1).PoI = [0 0 0];  % kg*mm^2
smiData.Solid(1).color = [1 1 0.75294117647058822];
smiData.Solid(1).opacity = 1;
smiData.Solid(1).ID = 'link 4*:*Default';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(2).mass = 0.45127899491723372;  % kg
smiData.Solid(2).CoM = [22.6523215568212 -0.30570340088881309 19.892456147505371];  % mm
smiData.Solid(2).MoI = [359.03379625323714 788.17291532322804 996.35642660406791];  % kg*mm^2
smiData.Solid(2).PoI = [0.67359710854375443 42.918796356587571 10.087796319101454];  % kg*mm^2
smiData.Solid(2).color = [0.90980392156862744 0.44313725490196076 0.031372549019607843];
smiData.Solid(2).opacity = 1;
smiData.Solid(2).ID = 'de robot*:*Default';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(3).mass = 0.11006396743101743;  % kg
smiData.Solid(3).CoM = [-49.344599044230172 -1.0889025961322174 1.682963098974548e-07];  % mm
smiData.Solid(3).MoI = [21.883277304627853 106.74914736384478 107.66675238383844];  % kg*mm^2
smiData.Solid(3).PoI = [1.5895694328402935e-05 -1.0567944899146482e-06 -1.8735062315893121];  % kg*mm^2
smiData.Solid(3).color = [1 0.50196078431372548 0.50196078431372548];
smiData.Solid(3).opacity = 1;
smiData.Solid(3).ID = 'link 2*:*Default';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(4).mass = 0.29989904917563825;  % kg
smiData.Solid(4).CoM = [30.18063322388689 49.417778115825087 0.00056414681720609908];  % mm
smiData.Solid(4).MoI = [464.91033592469864 282.3922535745595 584.38822100635684];  % kg*mm^2
smiData.Solid(4).PoI = [-0.0014306139949569364 -0.00063914634128658043 -192.93975040023452];  % kg*mm^2
smiData.Solid(4).color = [1 1 0.50196078431372548];
smiData.Solid(4).opacity = 1;
smiData.Solid(4).ID = 'link 1*:*Default';

%Inertia Type - Custom
%Visual Properties - Simple
smiData.Solid(5).mass = 0.055235243708882498;  % kg
smiData.Solid(5).CoM = [-58.397069111452531 -8.8022935747548407e-08 3.0571005069556778e-08];  % mm
smiData.Solid(5).MoI = [7.2414219215198541 67.372430886930758 63.742900802549862];  % kg*mm^2
smiData.Solid(5).PoI = [6.2658671320320618e-05 6.6342363953710718e-08 -1.6090010537030245e-07];  % kg*mm^2
smiData.Solid(5).color = [0.50196078431372548 1 0.50196078431372548];
smiData.Solid(5).opacity = 1;
smiData.Solid(5).ID = 'link 3*:*Default';


%============= Joint =============%
%X Revolute Primitive (Rx) %Y Revolute Primitive (Ry) %Z Revolute Primitive (Rz)
%X Prismatic Primitive (Px) %Y Prismatic Primitive (Py) %Z Prismatic Primitive (Pz) %Spherical Primitive (S)
%Constant Velocity Primitive (CV) %Lead Screw Primitive (LS)
%Position Target (Pos)

%Initialize the RevoluteJoint structure array by filling in null values.
smiData.RevoluteJoint(4).Rz.Pos = 0.0;
smiData.RevoluteJoint(4).ID = '';

smiData.RevoluteJoint(1).Rz.Pos = 13.253145643109933;  % deg
smiData.RevoluteJoint(1).ID = '[link 1-1:-:link 2-1]';

smiData.RevoluteJoint(2).Rz.Pos = -4.2826965346939847;  % deg
smiData.RevoluteJoint(2).ID = '[link 2-1:-:link 3-1]';

smiData.RevoluteJoint(3).Rz.Pos = -0.11639720437961928;  % deg
smiData.RevoluteJoint(3).ID = '[link 3-1:-:link 4-1]';

smiData.RevoluteJoint(4).Rz.Pos = 48.928540565305305;  % deg
smiData.RevoluteJoint(4).ID = '[de robot-1:-:link 1-1]';

