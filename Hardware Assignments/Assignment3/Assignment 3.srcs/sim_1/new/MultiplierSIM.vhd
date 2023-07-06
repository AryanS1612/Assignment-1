----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/11/2022 01:45:43 PM
-- Design Name: 
-- Module Name: MultiplierSIM - Behavioral
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

entity MultiplierSIM is
--  Port ( );
end MultiplierSIM;

architecture Behavioral of MultiplierSIM is

component Multiplier
  Port (clk : in std_logic;
  output : out std_logic_vector(15 downto 0));
end component;

component dist_mem_gen_1
    Port(a : std_logic_vector(13 downto 0);
    clk : in std_logic;
    d : in std_logic_vector(15 downto 0);
    we : in std_logic;
    spo : out std_logic_vector(15 downto 0));
end component;

signal clk : std_logic:='0';
signal output : std_logic_vector(15 downto 0);

begin
clk <= not clk after 5 ns;
UUT : Multiplier port map(clk=>clk, output=>output);

end Behavioral;
