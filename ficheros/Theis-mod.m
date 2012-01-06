function [s dsdT dsdS]= Theis(r,t,Q,T,S)
    %s=Q/(4piT)W(u); u=r^2S/(4Tt)
    if r<=.15
        r=.15;
    end
    
    u=r^2*S/T/t/4;


    if (nargout == 1)
        w=WTheis(u) ; 
        s=Q/4/pi/T*w;
    else
        [w dWdu]=WTheis(u) ; 
        s=Q/4/pi/T*w;
        %dsdT=Q/4/pi/T*(-w/T+dWdu*(-u/T)) ;
        dsdT=s*(-1/T + dWdu*(-u/T)/w);
        dsdS=s/w*dWdu*u/S ;
    end


end

function [W dW]= WTheis(u,du)
	% dW y du son opcionales

	if u>20 
	    if (nargout == 1)
		W=0;
	    else
		W=0;
		dW=0;
	    end
	    return
	elseif u>=1
	    err=1e-10;
	else
	    err=1e-6;
	end

	n=1. ;
	f=-u ;
	acumulador=f ;
	g=f ;

	if (nargout ~= 1) 
	    acumulador2= -1. ;
	    dg= -1.; 
	end

	if (nargout == 1)

	    while abs(g) >= err
		n=n+1 ;
		f=-f*u/n ;
		g=f/n ;
		acumulador=acumulador+g ;
	    end
	    W=-0.577215664901532860 -log(u) -acumulador ;
	else
	    while   (abs(g) >= err) && (abs(dg) >= err) 
		n=n+1 ;
		f=-f*u/n ;
		g=f/n ;
		dg=f/u ;
		acumulador=acumulador+g ;
		acumulador2=acumulador2+dg ;
	    end
	    W=-0.577215664901532860 -log(u) -acumulador ;
	    dW=-1./u-acumulador2 ;
	end

	if (nargin ~= 1) 
	    dW=dW*du ;
	end
end