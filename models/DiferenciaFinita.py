import sys
sys.path.append("views")
sys.path.append("models")

import metodoSolucion
from scipy.special import kn,expn
import numpy as np
import controlador
import scipy

class DiferenciaFinita(metodoSolucion.metodoNumerico):

    def __init__(self, dominio, parametros, asociar=None):
        
        ##Lista de cardinales de los parametros que utiliza el metodo
        ##Parametros 0: S, parametro 1:T, parametro 2:c
        self.paramcard=[0,1]
        #### Llamar al constructor del metodo de solucion
        ## probar llamar al metodo padre        
        metodoSolucion.metodoNumerico.__init__(self,dominio,parametros, asociar)
        #print 'Se creo el loco hantush'
        ##Hasntush que no acepta barrera        
        self.aceptaBarrera=False       
        self.optimizaciones=['']

    def calcular(self,tiempos, ti, tf, nit, nix, niy, x, y):
        acuiT=float(self.listaParametros[0].valoresParametro.valor)
        acuiS=float(self.listaParametros[1].valoresParametro.valor)
        m=nix
        n=niy
        l=n*m
        i=range(m)
        j=range(n)
        A=np.identity(len(i)*len(j))

        if self.aceptaBarrera==True:
            Todoslospbombeo=self.dominio.obtenerPBombeoYVirtuales()            
        else:
            Todoslospbombeo=self.dominio.obtenerPozosdeBombeo()

        Q=[]
        for p in Todoslospbombeo:
            Q=np.concatenate(Q,p.ensayos[0].devolverBProc())        
            
        #creando los intervalos
        #Ax=np.zeros(1,m-1);
        Ax=np.zeros((1,m-1),float)
        #for j=1:m-1;
        for j in range(m-1):
            Ax[j]=x[j+1]-x[j]

        Ay=np.zeros((1,n-1),float)
        for i in range(n-1):
            Ay[i]=y[i+1]-y[i]

        #creando la matriz de transmisividad
        T=np.ones((1,len(x)*len(y)),float)*acuiT

        #creando matriz de niveles incial
        h0=np.zeros((niy,nix),float)
        for i in range(nix):
            for j in range(niy):                
                h0[j,i]=self.dominio.devolverH0(x[i],y[j])

        #Para el elemento 1,1
        ##Aca jess donde tenes que tirar lineas a bocha!
        A1=np.zeros((1,l),float)
        A1[0]=-1/Ax[0]*(2*(T[0]*T[n]/(T[0]+T[n])))-1/Ay[0]*(2*(T[0]*T[1]/(T[0]+T[1])))
        A1[1]=1/Ay[n-2]*(2*(T[0]*T[1]/(T[0]+T[1])))        
        A1[n]=1/Ax[m-2]*(2*(T[0]*T[n]/(T[0]+T[n])))
        A[0,0:l]=A1

        #Para el elemento n,1
        An=np.zeros((1,l),float)
        An[n-1]=-1/Ax[0]*(2*(T[n-1]*T[n+n-1]/(T[n-1]+T[n+n-1])))-1/Ay[0]*(2*(T[n-1]*T[n-2]/(T[n-1]+T[n-2])))
        An[n-2]=1/Ay[0]*(2*(T[n-1]*T[n-2]/(T[n-1]+T[n-2])))
        An[n+n-1]=1/Ax[0]*(2*(T[n-1]*T[n+n-1]/(T[n-1]+T[n+n-1])))
        A[n-1,0:l]=An

        #Para los elementos comprendidos entre 1,2 y 1,m-1     
        for k in range(1,m-1):
            A[k*n,k*n]=-1/Ay[n-2]*(2*(T[k*n]*T[k*n+1]/(T[k*n]+T[k*n+1])))
            A[k*n,k*n+1]=1/Ay[n-2]*(2*(T[k*n]*T[k*n+1]/(T[k*n]+T[k*n+1])))

        #Para el elemento 1,m
        Am=np.zeros((1,l),float)
        Am[l-n]=-1/Ax[m-2]*(2*(T[l-2*n]*T[l-n]/(T[l-2*n]+T[l-n])))-1/Ay[n-2]*(2*(T[l-n+1]*T[l-n]/(T[l-n+1]+T[l-n])))
        Am[l-2*n]=1/Ax[m-2]*(2*(T[l-2*n]*T[l-n]/(T[l-2*n]+T[l-n])))
        Am[l-n+1]=1/Ay[n-2]*(2*(T[l-n+1]*T[l-n]/(T[l-n+1]+T[l-n])))
        A[l-n,0:l]=Am

        #Para los elementos comprendidos entre 2,m y n-1,m 
        for k in range(n-2):
            A[l-n+1+k,l-n+1+k]=-1/Ax[m-2]*(2*(T[l-n+1+k]*T[l-2*n+1+k]/(T[l-n+1+k]+T[l-2*n+1+k])))
            A[l-n+1+k,l-2*n+1+k]=1/Ax[m-2]*(2*(T[l-n+1+k]*T[l-2*n+1+k]/(T[l-n+1+k]+T[l-2*n+1+k])))

        #Para el elemento n,m
        Anm=np.zeros((1,l),float)
        Anm[l-1]=-1/Ax[m-2]*(2*(T[l-1]*T[l-n-1]/(T[l-1]+T[l-n-1])))-1/Ay[0]*(2*(T[l-1]*T[l-2]/(T[l-1]+T[l-2])))
        Anm[l-2]=1/Ay[0]*(2*(T[l-1]*T[l-2]/(T[l-1]+T[l-2])))
        Anm[l-n-1]=1/Ax[m-2]*(2*(T[l-1]*T[l-n-1]/(T[l-1]+T[l-n-1])))
        A[l-1,0:l]=Anm

        #Para los elementos comprendidos entre 2,1 y n-1,1 
        for k in range(n-2):
            A[k+1,k+1]=-1/Ax[0]*(2*(T[k+1]*T[k+n+1]/(T[k+1]+T[k+n+1])))
            A[k+1,k+n+1]=1/Ax[0]*(2*(T[k+1]*T[k+n+1]/(T[k+1]+T[k+n+1])))

        #Para los elementos comprendidos entre n,2 y n,m-1 
        for k in range(1,m-1):
            A[(1+k)*n-1,(1+k)*n-1]=-1/Ay[0]*(2*(T[(1+k)*n-1]*T[(1+k)*n-2])/(T[(1+k)*n-1]+T[(1+k)*n-2]))
            A[(1+k)*n-1,(1+k)*n-2]=1/Ay[0]*(2*(T[(1+k)*n-1]*T[(1+k)*n-2])/(T[(1+k)*n-1]+T[(1+k)*n-2]))

        #Para los elementos comprendidos entre 2,2 y n-1,m-1 
        for i in range(1,m-1):
            for j in range(n-2):
                A[(i)*n+1+j,(i)*n+1+j]=-1/Ax[i-1]*2/(Ax[i-1]+Ax[i])*(2*(T[(i)*n+1+j]*T[(i)*n+1+j-n]/(T[(i)*n+1+j]+T[(i)*n+1+j-n])))-(1/Ax[i])*2/(Ax[i-1]+Ax[i])*(2*(T[(i)*n+1+j]*T[(i)*n+1+j+n]/(T[(i)*n+1+j]+T[(i)*n+1+j+n])))+(-1/Ay[n-j-2])*2/(Ay[n-j-2]+Ay[n-j-1-2])*(2*(T[(i)*n+1+j]*T[(i)*n+j]/(T[(i)*n+1+j]+T[(i)*n+j])))-(1/Ay[n-j-1-2])*2/(Ay[n-j-2]+Ay[n-j-1-2])*(2*(T[(i)*n+1+j]*T[(i)*n+2+j]/(T[(i)*n+1+j]+T[(i)*n+2+j])))
                A[(i)*n+1+j,(i)*n+2+j]=(1/Ay[n-j-1-2])*2/(Ay[n-j-2]+Ay[n-j-1-2])*(2*(T[(i)*n+1+j]*T[(i)*n+2+j]/(T[(i)*n+1+j]+T[(i)*n+2+j])))
                #hasta ak revision
                A[(i)*n+1+j,(i)*n+j]=(1/Ay[n-j])*2/(Ay[n-j]+Ay[n-j-1])*(2*(T[(i)*n+1+j]*T[(i)*n+j]/(T[(i)*n+1+j]+T[(i)*n+j])))
                A[(i)*n+1+j,(i)*n+1+j-n]=(1/Ax[i])*2/(Ax[i]+Ax[i+1])*(2*(T[(i)*n+1+j]*T[(i)*n+1+j-n]/(T[(i)*n+1+j]+T[(i)*n+1+j-n])))
                A[(i)*n+1+j,(i)*n+1+j+n]=(1/Ax[i+1])*2/(Ax[i]+Ax[i+1])*(2*(T[(i)*n+1+j]*T[(i)*n+1+j+n]/(T[(i)*n+1+j]+T[(i)*n+1+j+n])))

        """S=np.identity(l,l)*acuiS

        x1=np.zeros((l,l),float)
        At=dt
        h=np.ones(l,1)*10
        for i in range(m-1):
            h[1+n*i:n+n*i,1]=h0[1:n,i+1]

        tetha=0.5
        E=A*tetha-S/(At)

        #Para los elementos conocidos
        for k in range(1,l-n+1,n):  #arriba
            E[k,1:l]=np.zeros(1,l)
            E[k,k]=1
            
        for k in range(l-n+1,l):    #derecha
            E[k,1:l]=np.zeros(1,l)
            E[k,k]=1

        for k in range((1,n),l,n):  #abajo
            E[k,1:l]=np.zeros(1,l)
            E[k,k]=1

        for k in range(1,n):        #izq
            E[k,1:l]=np.zeros(1,l)
            E[k,k]=1
            
        B=numpy.power(E,-1)

        for t1 in range(time):
            b(1:l)=0
            for i in range(Np):       
                xp=xps[i]
                yp=yps[i]
                b2=self.generab(lx,ly,Ax,Ay,n,m,xp,yp,l,x,y)
                Qt=Q[i]
                b=b+b2*Qt
            b1=(A*(tetha-1)-S/(At))*h+b        
            b1(1:n:l-n+1)=h0(1,1:m)   #arriba
            b1(l-n+1:l)=h0(1:n,m)     #derecha
            b1(n:n:l)=h0(n,1:m)       #abajo
            b1(1:n)=h0(1:n,1)         #izq

            h=B*b1
            x2[t1,1:l]=h"""

        ##Esto va a lo ultimo de todo y esta en otros scripts de Matlab

        ##Obtener todos los pozos de observacion
        TodoslospozosObservacion=d.obtenerPozosdeObservacion()
        ##Se instancias de una para todos los tiempos una lista de Observaciones solucionadas para cada pozo de observacion
        for pozoObservacion in TodoslospozosObservacion:
            pozoObservacion.instanciarSolucionadas(d.calcularH0(pozoObservacion.x, pozoObservacion.y), tiempos)

            xo=pozoObservacion.x
            yo=pozoObservacion.y
            pb=np.zeros((2,2),float)
            for j in range(m):
                if xo<x[j]:
                    pb[0,0]=x[j-1]
                    pb[0,1]=x[j]
                    break
            for i in range(n):
                if yo<y[i]:
                    pb[1,0]=y[i-1]
                    pb[1,1]=y[i]
                    break
            io=i
            jo=j
            
        self.matrizDescenso=np.zeros((len(tiempos),n,m), float)
        self.gyh=np.zeros((len(tiempos),n,m), float)
        self.gxh=np.zeros((len(tiempos),n,m), float)       
        
        for i in range(len(tiempos)):
            #de 0 a l-1 igual que matlab de 1 a l
            x1=x2[i,0:l];
            for k in range(n):
                #hr(k+1,1:m)=x1(k+1:n:l-n+k+1);
                #g(1:2:6) -> g[0:6:2]
                self.matrizDescenso[i,k,0:m]=x1[k:l-n+k+1:n]                
                #[gxh(:,:,i),gyh(:,:,i)] = gradient(-hr(:,:),Ax(1),Ay(1));
                [self.gyh[i,:,:],self.gxh[i,:,:]] = np.gradient(-self.matrizDescenso[i,:,:],Ax[0],Ay[0])

                for j in range(m):
                    if self.matrizDescenso[i,k,j]>self.max:
                        self.max=self.matrizDescenso[i,k,j]
                    if self.matrizDescenso[i,k,j]<self.min:
                        self.min=self.matrizDescenso[i,k,j]

            #Calculo para todos los pozos de observacion
            for pozoObservacion in TodoslospozosObservacion:
                hs1=x1[io+n*(jo-1)]
                aa=io+n*(jo-1)
                #hs2=x1(io+n*(jo-1)-1);
                hs2=x1[io+n*(jo-1)-1]
                aa=(io+n*(jo-1)-1)
                hs3=x1[io+n*(jo-2)]
                aa=io+n*(jo-2)
                hs4=x1[io+n*(jo-2)-1]
                aa=(io+n*(jo-2)-1)
                #hsm(i,t)=(hs1+hs2+hs3+hs4)/4                
                #Se actualizan solo las observaciones solucionadas
                pozoObservacion.obssolucionadas[i]=(hs1+hs2+hs3+hs4)/4              

        return self.matrizDescenso

    def generab(self,lx,ly,Ax,Ay,n,m,xp,yp,l,x,y):

        #b2(1:l)=0;
        b2=np.zeros((l),float)          
        pb=np.zeros((2,2),float)
        for j in range(m):
            if  xp<x[j]:
                pb[0,0]=x[j-1]
                pb[0,1]=x[j]
                break
            
        for i in range(n):
            if yp<y[i]:
                pb[1,0]=y[i-1]
                pb[1,1]=y[i]
                break

        #Luego las distancias a los nodos:
        d1=self.distancia(xp,yp,pb[0,1],pb[1,1])
        d2=self.distancia(xp,yp,pb[0,0],pb[1,1])
        d3=self.distancia(xp,yp,pb[0,1],pb[1,0])
        d4=sel.fdistancia(xp,yp,pb[0,0],pb[1,0])
        d=[d1,d2,d3,d4]
        
        for k in range(4):
            if d[k]<min(Ax)/100 or d[k]<min(Ay)/100:
                ff=np.zeros((1,4),float)
                ff[k]=1
                break
            else:
                ff[0]=(1/d1)/(1/d1+1/d2+1/d3+1/d4)
                ff[1]=(1/d2)/(1/d1+1/d2+1/d3+1/d4)
                ff[2]=(1/d3)/(1/d1+1/d2+1/d3+1/d4)
                ff[3]=(1/d4)/(1/d1+1/d2+1/d3+1/d4)

        b2[i+n*(j-1)]=ff[0]/((pb[0,1]-pb[0,0])*(pb[1,1]-pb[1,0]))
        b2[i+n*(j-1)-1]=ff[1]/((pb[0,1]-pb[0,0])*(pb[1,1]-pb[1,0]))
        b2[i+n*(j-2)]=ff[2]/((pb[0,1]-pb[0,0])*(pb[1,1]-pb[1,0]))
        b2[i+n*(j-2)-1]=ff[3]/((pb[0,1]-pb[0,0])*(pb[1,1]-pb[1,0]))

        return b2

    

    def distancia( x1,y1,x2,y2 ):
        
        d=np.sqrt(np.square(x1-x2) + np.square(y1-y2))
        return d
           

if __name__ == "__main__":
    cont=1
    ui = Hantush(cont,1)
    s=ui.calcularpozoGenerico(1,0.2,500,1000,0.0001,600)
    print s

    


