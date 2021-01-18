Option Explicit On
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst

Sub Main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim MotionMgr As SwMotionStudy.MotionStudyManager
    Dim MotionStudy As SwMotionStudy.MotionStudy
    Dim MotionStudyResults As SwMotionStudy.CosmosMotionStudyResults
    Dim status As Boolean
    Dim swSimPlotFeatureData As SldWorks.MotionPlotFeatureData
    Dim swSimPlotXAxisFeatureData As SldWorks.MotionPlotAxisFeatureData
    Dim swSimPlotYAxisFeatureData(0 To 1) As SldWorks.MotionPlotAxisFeatureData
    Dim swFace(0 To 0) As SldWorks.Face2
    Dim swFaceArray As Object
    Dim swYAxisArray As Object
    Dim PlotOutput As SwMotionStudy.MotionPlotFeatureOutput
    Dim swPlotFeature1 As SldWorks.Feature
    Dim swPlotFeature2 As SldWorks.Feature
    Dim swXData As Object
    Dim swYData As Object
    Dim nameYAxis(0 To 1) As String
    Dim i As Long
    Dim j As Long

    swModel = swApp.ActiveDoc
    swSelMgr = swModel.SelectionManager
    swModelDocExt = swModel.Extension

    ' Select the faces for which to calculate
    ' motion analysis, then calculate it and
    ' get the results
    status = swModelDocExt.SelectByID2("", "FACE", 0.03426699306681, 0.03342024416822, 0.02599934303839, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0.03047373686337, 0.006937653650944, 0.02566622869226, True, 0, Nothing, 0)
    MotionMgr = swModelDocExt.GetMotionStudyManager()
    MotionStudy = MotionMgr.GetMotionStudy("1200")
    status = MotionStudy.Calculate
    MotionStudyResults = MotionStudy.GetResults(4)

    ' Create a plot feature data and create the  x and y axes feature data
    swSimPlotFeatureData = MotionStudyResults.CreatePlotFeatureData()
    swSimPlotXAxisFeatureData = MotionStudyResults.CreatePlotXAxisFeatureData()
    swSimPlotYAxisFeatureData(0) = MotionStudyResults.CreatePlotYAxisFeatureData()
    swSimPlotYAxisFeatureData(1) = MotionStudyResults.CreatePlotYAxisFeatureData()
    ' Set the type of plots
    nameYAxis(0) = "swMotionPlotAxisType_TRANS_DISP"
    swSimPlotYAxisFeatureData(0).Type = SwConst.swMotionPlotAxisType_TRANS_VELOCITY
    swSimPlotYAxisFeatureData(0).Component = 1
    nameYAxis(1) = "swMotionPlotAxisType_TRANS_VELOCITY"
    swSimPlotYAxisFeatureData(1).Type = SwConst.swMotionPlotAxisType_TRANS_VELOCITY
    swSimPlotYAxisFeatureData(1).Component = 1

    ' Get the entity whose motion you want analyzed
    swFace(0) = swSelMgr.GetSelectedObject6(1, -1)
    swFaceArray = swFace
    swSimPlotYAxisFeatureData(0).Entities = swFaceArray
    swSimPlotYAxisFeatureData(1).Entities = swFaceArray
    ' Get the plot's x-axis and y-axes values
    swYAxisArray = swSimPlotYAxisFeatureData
    PlotOutput = MotionStudyResults.GetValues(swSimPlotFeatureData, swSimPlotXAxisFeatureData, (swYAxisArray))
    swXData = PlotOutput.GetXAxis()

    ' Print the x-axis values and the y-axis translational
    ' displacement values and the y-axes translational velocity
    ' values to the Immediate window
    'Debug.Print ""
    For i = 0 To UBound(swYAxisArray)
        'Debug.Print "------ YAxis Type : " & nameYAxis(i)
        swYData = PlotOutput.GetYAxis(swSimPlotYAxisFeatureData(i))
        For j = 0 To UBound(swXData)
            'Debug.Print " (x, y) : (" & Strings.Format(swXData(j)) & ", " & swYData(j) & ")"

        Next j

    Next i

    ' Insert and display the translational displacement plot
    swPlotFeature1 = MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData(0))
    'Debug.Print "Name of plot feature: " & swPlotFeature1.Name
    ' Insert and display the translational velocity plot
    swPlotFeature2 = MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData(1))
    'Debug.Print "Name of plot feature: " & swPlotFeature2.Name
End Sub