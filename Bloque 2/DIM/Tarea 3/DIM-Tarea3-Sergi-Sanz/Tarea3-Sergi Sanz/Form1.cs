using System;
using System.Drawing;
using System.Windows.Forms;
using System.Speech.Recognition;
using System.Speech.Synthesis;
using System.Globalization;
using System.Threading;
using System.Media;
using System.IO;
using System.Windows.Media;

namespace REcoSample
{
    
    public partial class Form1 : Form
    {
        private System.Speech.Recognition.SpeechRecognitionEngine _recognizer =
           new SpeechRecognitionEngine();
        private SpeechSynthesizer synth = new SpeechSynthesizer();
        
        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            Grammar grammar = CreateGrammarBuilderRGBSemantics2(null);
            _recognizer.SetInputToDefaultAudioDevice();
            _recognizer.UnloadAllGrammars();
            _recognizer.UpdateRecognizerSetting("CFGConfidenceRejectionThreshold", 60);
            grammar.Enabled = true;
            _recognizer.LoadGrammar(grammar);
            _recognizer.SpeechRecognized += new EventHandler<SpeechRecognizedEventArgs>(_recognizer_SpeechRecognized);
            //reconocimiento asíncrono y múltiples veces
            _recognizer.RecognizeAsync(RecognizeMode.Multiple);

            synth.Speak("Bienvenido a nuestro hogar");
        }

        void Accion(bool info, string persona)
        {
            switch (persona.ToUpper())
            {
                case "JARDIN":
                    if (imgCasaVolver.Visible == true || museo.Visible == true) { imgCasaVolver.Visible = false; museo.Visible = false; }
                    imgJardin.Visible = true;
                    break;

                case "NIÑOS":
                    ninos.Visible = true;
                    break;

                case "CASA":
                    if(imgJardin.Visible == true || museo.Visible == true) { imgJardin.Visible = false; museo.Visible = false; }
                    imgCasaVolver.Visible = true;
                    ninos.Visible = false;
                    break;
                case "JARBIS":
                    if (info == false) { synth.Speak("Adios señor"); Application.Exit(); }
                    else if (info == true) { synth.Speak("Bienvenido señor"); }
                    break;
                case "MUSEO":
                    if (imgJardin.Visible == true || imgCasaVolver.Visible == true) { imgJardin.Visible = false; imgCasaVolver.Visible = false; }
                    museo.Visible = true;
                    ninos.Visible = false;
                    break;
                case "CHISTES":
                    Random rnd = new Random();
                    int random = rnd.Next(1, 3);
                    if(random == 1) { synth.Speak("¿Por qué estás hablando con esas zapatillas? Porque pone converse"); }
                    else if(random == 2){ synth.Speak("¿Qué le dice un techo a otro ? Techo de menos."); }
                    else if(random == 3) { synth.Speak("Mama en el cole me llaman despistado , Niño que esta no es tu casa"); }
                    break;
            }
        }



        
        void _recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            //obtenemos un diccionario con los elementos semánticos
            SemanticValue semantics = e.Result.Semantics;

            string rawText = e.Result.Text;
            RecognitionResult result = e.Result;

            if (semantics.ContainsKey("eventos"))
            {
                switch ((string)semantics["eventos"].Value)
                {
                    case "E":
                        Accion(true, (string)semantics["participantes"].Value);
                        break;
                    case "S":
                        Accion(true, (string)semantics["participantes"].Value);
                        break;
                    case "N":
                        Accion(true, (string)semantics["participantes"].Value);
                        break;
                    case "A":
                        Accion(false, (string)semantics["participantes"].Value); 
                        break;
                    case "H":
                        Accion(true, (string)semantics["participantes"].Value);
                        break;
                    case "V":
                        Accion(true, (string)semantics["participantes"].Value);
                        break;
                    case "C":
                        Accion(true, (string)semantics["participantes"].Value);
                        break;
                }

            }

            synth.Speak(rawText);
            pizarra.Text = rawText;
        }


        private Grammar CreateGrammarBuilderRGBSemantics2(params int[] info)
        {
            Choices escuelaChoice = new Choices();

            SemanticResultValue choiceResultValue =
                    new SemanticResultValue("Jardin", "jardin");
            GrammarBuilder resultValueBuilder = new GrammarBuilder(choiceResultValue);
            escuelaChoice.Add(resultValueBuilder);

            choiceResultValue =
                   new SemanticResultValue("Casa", "casa");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            escuelaChoice.Add(resultValueBuilder);

            choiceResultValue =
                    new SemanticResultValue("Niños", "niños");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            escuelaChoice.Add(resultValueBuilder);

            choiceResultValue =
                    new SemanticResultValue("Jarbis", "jarbis");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            escuelaChoice.Add(resultValueBuilder);

            choiceResultValue =
            new SemanticResultValue("Museo", "museo");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            escuelaChoice.Add(resultValueBuilder);

            choiceResultValue =
                new SemanticResultValue("Chiste", "chistes");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            escuelaChoice.Add(resultValueBuilder);

            SemanticResultKey choiceResultKey = new SemanticResultKey("participantes", escuelaChoice);
            GrammarBuilder participantes = new GrammarBuilder(choiceResultKey);

            Choices EventosChoice = new Choices();

            choiceResultValue =
                    new SemanticResultValue("Ir", "E");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultValue =
                    new SemanticResultValue("Volver", "S");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultValue =
                        new SemanticResultValue("Jugar", "N");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultValue =
            new SemanticResultValue("Adios", "A");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultValue =
                new SemanticResultValue("Hola", "H");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultValue =
                new SemanticResultValue("Visitar", "V");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultValue =
               new SemanticResultValue("Contar", "C");
            resultValueBuilder = new GrammarBuilder(choiceResultValue);
            EventosChoice.Add(resultValueBuilder);

            choiceResultKey = new SemanticResultKey("eventos", EventosChoice);
            GrammarBuilder eventos = new GrammarBuilder(choiceResultKey);

            GrammarBuilder frase = new GrammarBuilder();
            frase.Append(eventos);
            frase.Append(participantes);
//            frase.AppendDictation();

            Grammar grammar = new Grammar(frase);
            grammar.Name = "Casa";
            return grammar;

        }
    }
}