function [s]= Theis(r,t,Q,T,S)
    %s=Q/(4piT)W(u); u=r^2S/(4Tt)
    if r<=.15
        r=.15;
    end
    
    s=r^2*S/T/t/4;
    



end

