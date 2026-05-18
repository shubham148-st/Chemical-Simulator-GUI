package Splitter1

  model ms
    extends Simulator.Streams.MaterialStream;
    extends Simulator.Files.ThermodynamicPackages.RaoultsLaw;
  end ms;

  model Splitter1Simulation 
    import data = Simulator.Files.ChemsepDatabase;
    parameter data.Bromine Bromine;
    parameter data.Carbontetrachloride Carbontetrachloride;
    parameter Integer Nc = 2;
    parameter data.GeneralProperties C[Nc] = {Bromine, Carbontetrachloride};
    ms MaterialStream1(Nc = 2, C = {Bromine, Carbontetrachloride});
    Simulator.UnitOperations.Splitter Splitter1(Nc = 2,C = {Bromine, Carbontetrachloride}, No = 2, CalcType = "Split_Ratio", SpecVal_s = {0.5, 0.5});

    Simulator.UnitOperations.Cooler Cooler1(Nc = 2,C = {Bromine, Carbontetrachloride}, Pdel = 0, Eff = 1);


  equation
MaterialStream1.P = 101325;
MaterialStream1.T = 300;
MaterialStream1.F_p[1] = 100;
connect(Splitter1.In, MaterialStream1.Out);
connect(Splitter1.Out, Cooler1.In);
connect(Cooler1.In, Splitter1.Out);
connect(Cooler1.Out, MaterialStream1.In);
Cooler1.Q = None;
  end Splitter1Simulation;
end Splitter1;
