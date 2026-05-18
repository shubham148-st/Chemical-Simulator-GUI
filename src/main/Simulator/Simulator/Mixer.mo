package Mixer
 
  model ms
    extends Simulator.Streams.MaterialStream;
    extends Simulator.Files.ThermodynamicPackages.RaoultsLaw;
  end ms;

  model MixerSimulation 
    import data = Simulator.Files.ChemsepDatabase;
    parameter data.Bromine Bromine;
    parameter data.Carbontetrachloride Carbontetrachloride;
    parameter Integer Nc = 2;
    parameter data.GeneralProperties C[Nc] = {Bromine, Carbontetrachloride};
    ms MaterialStream1(Nc = 2, C = {Bromine, Carbontetrachloride});
    ms MaterialStream2(Nc = 2, C = {Bromine, Carbontetrachloride});
    ms MaterialStream3(Nc = 2, C = {Bromine, Carbontetrachloride});

    Simulator.UnitOperations.Mixer Mixer1(Nc = 2,C = {Bromine, Carbontetrachloride}, NI = 2, outPress = "Inlet_Average");
   
   
  equation
    connect(MaterialStream1.Out, Mixer1.In[1]);
    connect(MaterialStream2.Out, Mixer1.In[2]);
    connect(Mixer1.Out, MaterialStream3.In);
    
    MaterialStream1.P = 101325;
    MaterialStream1.T = 300;
    MaterialStream1.F_p[1] = 100;
    MaterialStream2.P = 101325;
    MaterialStream2.T = 300;
    MaterialStream2.F_p[1] = 100;
    MaterialStream1.x_pc[1, :] = {1, 0};
    MaterialStream2.x_pc[1, :] = {0, 1};
  end MixerSimulation;
end Mixer;
