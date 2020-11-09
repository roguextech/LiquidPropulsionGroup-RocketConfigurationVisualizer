%% Pressurization
% 
clc, clear all
%% Upper and Lower Bounds
% Known values
P_HE = 12.4e6;                  % [Pa]
P_Reg = 2.279e6;                % [Pa], Regulator Pressure
T1 = 300;                       % [K]
R_HE = 2.0769;                  % [kJ/kg*K], Gas constant
Vol_HE = 49;                    % [L]
Vol_HE = Vol_HE*1e-3;           % [m^3]
Vol_LOX = 7.8;                  % [L]
Vol_LOX = Vol_LOX*1e-3;         % [m^3]
Vol_RP1 = 7.8;                  % [L]
Vol_RP1 = Vol_RP1*1e-3;         % [m^3]
Vol_OF = Vol_LOX + Vol_RP1;                 % [m^3], Combined Vol of O/F tanks
Vol_Comb = Vol_HE + Vol_LOX + Vol_RP1;      % [m^3], Combined Vol of all 3 tanks

% Conservative Calculations
% Lower Bound
% The condition where the regulator does not exist, and the HE volume
% expands to fill the entire system.
P_f = P_HE*Vol_HE/Vol_Comb;     % [kPa], final pressure conservative
P_f = P_f / 6895;               % [psi]
fprintf('The lower bound supply pressure post-combustion is approx. %1.4f psi.\n',P_f)

% Optimistic Calculations
% Upper Bound
% The condition where the pressurant is released slowly enough that the
% temperature remains constant throughout the process (non adiabatic), and 
% the regulator is ideal, acting as a constant pressure source.
N_HE = P_HE*Vol_HE/R_HE/T1;     % [mol], moles of HE in the HE tank alone
N_OF = P_Reg*Vol_OF/R_HE/T1;    % [mol], moles of HE in the OF tank alone
Ndiff = N_HE - N_OF;            % [mol]
P_f = Ndiff*R_HE*T1/Vol_HE;     % [kPa], final pressure optimistic
P_f = P_f / 6895;               % [psi]
fprintf('The upper bound supply pressure post-combustion is approx. %1.4f psi.\n',P_f)

% A value between these bounds is a boundary value for the differential
% equation describing the behavior of the supply pressure during activity.

% The lower bound allows the most pressure across the regulator, and thus
% is the worst case for the supply pressure's effect on the chamber
% pressure.




