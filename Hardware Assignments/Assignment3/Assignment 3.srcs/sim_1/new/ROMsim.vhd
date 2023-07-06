----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/07/2022 02:32:08 PM
-- Design Name: 
-- Module Name: ROMsim - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity ROMsim is
--  Port ( );
end ROMsim;

architecture Behavioral of ROMsim is

component dist_mem_gen_0
Port(a : in std_logic_vector(13 downto 0) := "00000000000000";
clk : in std_logic;
spo : out std_logic_vector(7 downto 0));
end component;
signal a : std_logic_vector(13 downto 0); 
signal c : std_logic := '0';
signal o : std_logic_vector(7 downto 0);

begin
c <= not c after 10 ns;
a <= "00000000000000", "00000000000001" after 50 ns, "00000000000010" after 100 ns;
UUT : dist_mem_gen_0 port map(clk=>c, a=>a, spo=>o);



end Behavioral;
