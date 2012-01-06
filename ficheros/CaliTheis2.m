function [T S f_min obs_sim ]=CaliTheis2(Q,obs,r_obs,t_obs,Tmin,Tmax,Smin,Smax)


%Parametros
N_int_T=10;
N_int_S=10;
N_ref_max=20;
esc_ref=.5;


N_obs=length(obs);
obs_sim(N_obs)=0;


T_vec(N_int_T)=0;
S_vec(N_int_S)=0;

Tinf=Tmin;
Tsup=Tmax;
Sinf=Smin;
Ssup=Smax;

ref=0;

while ref < N_ref_max
    
    DT=Tsup-Tinf;
    DS=Ssup-Sinf;
    
    auxT=DT/(N_int_T-1);
    for i=1:N_int_T
        T_vec(i)=Tinf +(i-1)*auxT;
    end
    
    auxS=DS/(N_int_S-1);
    for i=1:N_int_S
        S_vec(i)=Sinf +(i-1)*auxS;
    end

    
    f_min=realmax;
    
    for i=1:N_int_T
        for j=1:N_int_S
            f=0;
            for k=1:N_obs
                obs_sim(k) = Theis(r_obs(k),t_obs(k),Q,T_vec(i),S_vec(j));
                f=f+(obs_sim(k)-obs(k))^2/obs(k)^2;
            end
            
            if f<f_min
                f_min=f;
                T=T_vec(i);
                S=S_vec(j);
            end
             
        end
    end
    
    DT=DT*esc_ref;
    
    if T-DT/2 <Tmin
        Tinf=Tmin;
        Tsup=Tmin+DT;
    elseif  T+DT/2 >Tmax
        Tsup=Tmax;
        Tmin=Tmax-DT;
    else
        Tsup=T+DT/2;
        Tmin=T-DT/2;
    end
    
    
    DS=DS*esc_ref;
    if S-DS/2 <Smin
        Sinf=Smin;
        Ssup=Smin+DS;
    elseif  S+DS/2 >Smax
        Ssup=Smax;
        Smin=Smax-DS;
    else
        Ssup=S+DS/2;
        Smin=S-DS/2;
    end
    
    ref=ref+1;
end










end
