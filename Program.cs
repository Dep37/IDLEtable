   
   
    namespace Idle
    {
        
        public class ReadBin
        {

            public static void Main()
            {

                using (BinaryReader reader = new BinaryReader(File.Open(@"plc.bin", FileMode.Open)))

                    while (reader.PeekChar() > -1)
                        {
                            double rp_idle = reader.ReadInt32();
                            Console.WriteLine(rp_idle);
                        }

            }

        }

    }
