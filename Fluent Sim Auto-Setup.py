# encoding: utf-8
# Release 19.1
# Adapted by BOT Yokel
SetScriptVersion(Version="19.1.103")
template1 = GetTemplate(TemplateName="FLUENT")

'''
Instructions:
1. Enter the file path containing the Fluent case files under directory. Change all backslashes in the file path to forward slashes
e.g. directory = "C:/Users/tom/Documents/DV2 Nose Study/Group 3"
2. Enter the names of the case files without the .cas extension under filenames
3. Enter the reference length (m) for each case file under lengths. The order of the reference lengths should match the order of the filenames
4. Enter the reference area (m^2) for each case file under areas. The order of the reference areas should match the order of the filenames
5. Enter the number of case files to be set up under num_sims
'''

directory = "INSERT_HERE"

filenames = [
"INSERT_HERE",
"INSERT_HERE"
]

lengths = [
"INSERT_HERE",
"INSERT_HERE"
]

areas = [
"INSERT_HERE",
"INSERT_HERE"
]

num_sims = 0


# Range is number of sims to set up
for num in range(num_sims):
        system1 = template1.CreateSystem()
        system1.DisplayText = "{}".format(filenames[num])
        setup1 = system1.GetContainer(ComponentName="Setup")
        fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()
        fluentLauncherSettings1.SetEntityProperties(Properties=Set(Dimension="ThreeD", EnvPath={}, RunParallel=True, NumberOfProcessors=8))
        setup1.Edit()
        # Change file path for the next line, change all file path backslashes to forward slashes
        setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"MenuBar*ImportSubMenu*Case...\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/{}.cas\") \"Case Files (*.cas* *.msh* *.MSH* )\")".format(directory, filenames[num]))
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "General*Table1*ButtonBox1(Mesh)*PushButton1(Scale)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)\" '( 3))")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*DropDownList2(Mesh Was Created In)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*Table1*Table2(Scaling)*PushButton4(Scale)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Scale Mesh*PanelButtons*PushButton1(Close)")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Laminar)"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Laminar)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Laminar)"))(cx-gui-do cx-set-toggle-button2 "Viscous Model*Table1*ToggleBox1(Model)*k-omega (2 eqn)" #t)(cx-gui-do cx-activate-item "Viscous Model*Table1*ToggleBox1(Model)*k-omega (2 eqn)")(cx-gui-do cx-set-toggle-button2 "Viscous Model*Table1*ToggleBox7(k-omega Model)*SST" #t)(cx-gui-do cx-activate-item "Viscous Model*Table1*ToggleBox7(k-omega Model)*SST")(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Materials|Fluid|air\"))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry10\" '( 1.177))(cx-gui-do cx-set-real-entry-list \"Create/Edit Materials*RealEntry16\" '( 1.846e-05))")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton3(Change/Create)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|inlet (velocity-inlet, id=5)"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|inlet (velocity-inlet, id=5)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|inlet (velocity-inlet, id=5)\"))(cx-gui-do cx-set-real-entry-list \"Velocity Inlet*Frame3*Frame1(Momentum)*Table1*Table8*RealEntry2(Velocity Magnitude)\" '( 18))(cx-gui-do cx-activate-item \"Velocity Inlet*PanelButtons*PushButton1(OK)\")")
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|road (wall, id=7)"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|road (wall, id=7)"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Boundary Conditions|road (wall, id=7)\"))(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*ToggleBox1(Wall Motion)*Moving Wall\")(cx-gui-do cx-set-toggle-button2 \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\" #t)(cx-gui-do cx-activate-item \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table1*ToggleBox1*Absolute\")(cx-gui-do cx-set-real-entry-list \"Wall*Frame3*Frame1(Momentum)*Table1*Frame1*Frame1*Table1*Table2(Motion)*Table2*Table1*RealEntry2(Speed)\" '( 18))(cx-gui-do cx-activate-item \"Wall*PanelButtons*PushButton1(OK)\")")
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Reference Values"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Setup|Reference Values\"))(cx-gui-do cx-set-list-selections \"Reference Values*DropDownList1(Compute from)\" '( 3))")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Reference Values*DropDownList1(Compute from)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry1(Area)\")".format(areas[num]))
        setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\" '({}))(cx-gui-do cx-activate-item \"Reference Values*Table2(Reference Values)*RealEntry5(Length)\")".format(lengths[num]))
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Methods\"))(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)\" '( 3))")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table2(Pressure-Velocity Coupling)*DropDownList2(Scheme)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)\" '( 1))")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList2(Pressure)")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Solution Methods*Table1*CheckButton5(Pseudo Transient)" #t)(cx-gui-do cx-activate-item "Solution Methods*Table1*CheckButton5(Pseudo Transient)")(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Drag...")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Drag Report Definition*Table1*TextEntry3(Name)" "drag")(cx-gui-do cx-activate-item "Drag Report Definition*Table1*TextEntry3(Name)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*ToggleBox1(Report Output Type)*Drag Force\")(cx-gui-do cx-set-list-selections \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Drag Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Drag Report Definition*PanelButtons*PushButton1(OK)\")")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Force ReportSubMenu*Lift...")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table2*List2(Wall Zones)\")(cx-gui-do cx-set-text-entry \"Lift Report Definition*Table1*TextEntry3(Name)\" \"lift\")(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*TextEntry3(Name)\")")
        setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry2(Y)\" '( 0))(cx-gui-do cx-set-real-entry-list \"Lift Report Definition*Table1*Table1*Table2(Force Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*Table5(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Lift Report Definition*Table1*Table1*CheckButton6(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Lift Report Definition*PanelButtons*PushButton1(OK)\")")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Flux ReportSubMenu*Mass Flow Rate...")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Flux Report Definition*TextEntry1(Name)" "inlet-mass-flow-rate")(cx-gui-do cx-activate-item "Flux Report Definition*TextEntry1(Name)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Flux Report Definition*List3(Boundaries)\" '( 1))(cx-gui-do cx-activate-item \"Flux Report Definition*List3(Boundaries)\")(cx-gui-do cx-set-toggle-button2 \"Flux Report Definition*Table2*Table9(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Flux Report Definition*Table2*Table9(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Flux Report Definition*Table2*Table9(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Flux Report Definition*Table2*Table9(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Flux Report Definition*Table2*CheckButton10(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Flux Report Definition*Table2*CheckButton10(Create Output Parameter)\")(cx-gui-do cx-activate-item \"Flux Report Definition*PanelButtons*PushButton1(OK)\")")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*Flux ReportSubMenu*Mass Flow Rate...")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-text-entry "Flux Report Definition*TextEntry1(Name)" "outlet-mass-flow-rate")(cx-gui-do cx-activate-item "Flux Report Definition*TextEntry1(Name)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-toggle-button2 \"Flux Report Definition*Table2*Table9(Create)*CheckButton1(Report File)\" #t)(cx-gui-do cx-activate-item \"Flux Report Definition*Table2*Table9(Create)*CheckButton1(Report File)\")(cx-gui-do cx-set-toggle-button2 \"Flux Report Definition*Table2*Table9(Create)*CheckButton2(Report Plot)\" #t)(cx-gui-do cx-activate-item \"Flux Report Definition*Table2*Table9(Create)*CheckButton2(Report Plot)\")(cx-gui-do cx-set-toggle-button2 \"Flux Report Definition*Table2*CheckButton10(Create Output Parameter)\" #t)(cx-gui-do cx-activate-item \"Flux Report Definition*Table2*CheckButton10(Create Output Parameter)\")(cx-gui-do cx-set-list-selections \"Flux Report Definition*List3(Boundaries)\" '( 3))(cx-gui-do cx-activate-item \"Flux Report Definition*List3(Boundaries)\")(cx-gui-do cx-activate-item \"Flux Report Definition*PanelButtons*PushButton1(OK)\")")
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '( 0))(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '())(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '( 1))(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '())(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '( 3))(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '())(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '( 2))(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '())(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")(cx-gui-do cx-set-list-selections \"Report Definitions*Table1*List1(Report Definitions)\" '( 2))(cx-gui-do cx-activate-item \"Report Definitions*Table1*List1(Report Definitions)\")")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton2(Edit)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Lift Report Definition*PanelButtons*PushButton1(OK)")')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Report Definitions*PanelButtons*PushButton1(Close)")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-list-tree-selections \"NavigationPane*List_Tree1\" (list \"Solution|Run Calculation\"))(cx-gui-do cx-set-list-selections \"Run Calculation*Table1*Table5(Pseudo Transient Options)*Table1(Fluid Time Scale)*DropDownList3(Length Scale Method)\" '( 2))")
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Run Calculation*Table1*Table5(Pseudo Transient Options)*Table1(Fluid Time Scale)*DropDownList3(Length Scale Method)")')
        setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Run Calculation*Table1*Table5(Pseudo Transient Options)*Table1(Fluid Time Scale)*RealEntry5(Length Scale)\" '({}))(cx-gui-do cx-activate-item \"Run Calculation*Table1*Table5(Pseudo Transient Options)*Table1(Fluid Time Scale)*RealEntry5(Length Scale)\")".format(lengths[num]))
        setup1.SendCommand(Command='(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*IntegerEntry10(Number of Iterations)" 600)(cx-gui-do cx-activate-item "Run Calculation*Table1*IntegerEntry10(Number of Iterations)")')
        setup1.SendCommand(Command="/mesh/repair-improve/allow-repair-at-boundaries yes")
        setup1.SendCommand(Command="/mesh/repair-improve/include-local-polyhedra-conversion-in-repair yes")
        setup1.SendCommand(Command="/mesh/repair-improve/repair")
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")')
        setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))')
        setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
        Save(Overwrite=True)
