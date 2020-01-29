Public Class ConfigFile

    Public Property Port As Integer
    Public Property Username As String
    Public Property Password As String

    Public Sub SaveToFile(Path As String)
        Using File As New IO.FileStream(Path, IO.FileMode.Create)
            Dim Writer As New Xml.Serialization.XmlSerializer(GetType(ConfigFile))
            Writer.Serialize(File, Me)
        End Using
    End Sub

    Public Shared Function LoadFromFile(ByVal FilePath As String) As ConfigFile
        Using File As New IO.FileStream(FilePath, IO.FileMode.Open)
            Dim Reader As New Xml.Serialization.XmlSerializer(GetType(ConfigFile))
            Return DirectCast(Reader.Deserialize(File), ConfigFile)
        End Using
    End Function


End Class
