clear;
T=800;
S=1e-3;
Q=10;

%valors h
%[ 0.00180576  0.00244694  0.00311182  0.00350687  0.00390466  0.00418805]

%salta un error

N_obs=6;
r_obs=[179.63574254585305, 179.63574254585305, 179.63574254585305, 179.63574254585305, 179.63574254585305, 179.63574254585305];
t_obs=[0.1, 0.2, 0.4, 0.6, 0.9, 1.2];

obs(N_obs)=0;
for i=1:N_obs
    obs(i)= Theis(r_obs(i),t_obs(i),Q,T,S)
end

Tmin=500;
Tmax=1500;
Smin=1e-4;
Smax=1e-2;

[Tc Sc err obs_sim ]=CaliTheis2(Q,obs,r_obs,t_obs,Tmin,Tmax,Smin,Smax)
