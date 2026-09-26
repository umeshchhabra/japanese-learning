$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
Write-Output 'Speech assembly loaded.'
$lessonRoot = Split-Path -Parent $PSScriptRoot
$tracks = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'audio-scripts.json') -Raw -Encoding utf8 | ConvertFrom-Json
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
Write-Output 'Synthesizer created.'
$synth.SelectVoice('Microsoft Haruka Desktop')
Write-Output 'Japanese voice selected.'
$voiceNames = @($synth.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo.Name })
$secondVoice = if ($voiceNames -contains 'Microsoft Ichiro') { 'Microsoft Ichiro' } else { 'Microsoft Haruka Desktop' }
foreach ($track in $tracks) {
    foreach ($speed in @('normal','slow')) {
        $synth.Rate = if ($speed -eq 'slow') { -3 } else { 0 }
        $out = Join-Path $lessonRoot ('audio\' + $track.id + '-' + $speed + '.wav')
        $synth.SetOutputToWaveFile($out)
        $builder = New-Object System.Speech.Synthesis.PromptBuilder([System.Globalization.CultureInfo]::GetCultureInfo('ja-JP'))
        $builder.AppendBreak([TimeSpan]::FromMilliseconds(350))
        for ($i = 0; $i -lt $track.lines.Count; $i++) {
            $voice = if ($track.dialogue -and ($i % 2 -eq 1)) { $secondVoice } else { 'Microsoft Haruka Desktop' }
            $builder.StartVoice($voice)
            # Explicit kana pronunciation for topic particles in all-kana text.
            $spoken = $track.lines[$i].Replace('わたしは','わたしわ').Replace('コーヒーは','コーヒーわ').Replace('テレビは','テレビわ').Replace('どようびは','どようびわ').Replace('にちようびは','にちようびわ').Replace('ひるごはんは','ひるごはんわ')
            $builder.AppendText($spoken)
            $builder.EndVoice()
            $pause = if ($speed -eq 'slow') { 1200 } else { 750 }
            $builder.AppendBreak([TimeSpan]::FromMilliseconds($pause))
        }
        $synth.Speak($builder)
        $synth.SetOutputToNull()
        Write-Output ('Created ' + [System.IO.Path]::GetFileName($out))
    }
}
$synth.Dispose()
