clear;
T=800;
S=1e-3;
Q=10;


N_obs=10;
r_obs=[10 10 10 10 10 10 100 100 100 100];
t_obs=[.1 .2 .4 .6 .9 1.2 .9 1.2 1.8 2.5];

obs(N_obs)=0;
for i=1:N_obs
    obs(i)= Theis(r_obs(i),t_obs(i),Q,T,S);
end

%obs=obs.*(.95+.1*rand(1,N_obs));

Tmin=500;
Tmax=1500;
Smin=1e-4;
Smax=1e-2;


[Tc Sc err obs_sim ]=CaliTheis2(Q,obs,r_obs,t_obs,Tmin,Tmax,Smin,Smax)
obs