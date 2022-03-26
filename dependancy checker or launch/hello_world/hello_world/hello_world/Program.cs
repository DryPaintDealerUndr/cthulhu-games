using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using Twilio.TwiML.Voice;

namespace hello_world
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string result = "";
                Console.WriteLine("Checking Python...\nPress Enter to continue.");
                Console.ReadLine();
                ProcessStartInfo start = new ProcessStartInfo();
                start.FileName = @"python.exe"; // Specify exe name.
                start.Arguments = "--version";
                start.UseShellExecute = false;
                start.RedirectStandardOutput = true;
                start.CreateNoWindow = true;
                start.RedirectStandardInput = true;
                using (Process process = Process.Start(start))
                {
                    using (StreamReader reader = process.StandardOutput)
                    {
                        result = reader.ReadToEnd();
                        Console.WriteLine(result + "\nPress Enter to continue.");
                        Console.ReadLine();
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("No python installed!");
                Console.ReadLine();
                System.Environment.Exit(0);
            }
            try
            {
                string result = "";
                Console.WriteLine("Checking Python libraries...\nPress Enter to continue.");
                Console.ReadLine();
                ProcessStartInfo start = new ProcessStartInfo();
                start.FileName = @"python.exe"; // Specify exe name.
                start.Arguments = string.Format("{0}", Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "python.py"));
                start.UseShellExecute = false;
                start.RedirectStandardOutput = true;
                start.RedirectStandardError = true;
                start.CreateNoWindow = true;
                using (Process process = Process.Start(start))
                {
                    using (StreamReader reader = process.StandardOutput)
                    {
                        result = reader.ReadToEnd();
                        string err = process.StandardError.ReadToEnd();
                        Console.WriteLine(result + err + "\nPress Enter to continue.");
                        Console.ReadLine();
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Please install the Python dependancies in requirements.txt");
                Console.ReadLine();
                System.Environment.Exit(0);
            }
        }
        }
    }
