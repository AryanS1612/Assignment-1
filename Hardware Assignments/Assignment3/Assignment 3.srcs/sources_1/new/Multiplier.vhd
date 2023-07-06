----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 10/17/2022 03:48:16 PM
-- Design Name: 
-- Module Name: Multiplier - Behavioral
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

entity Multiplier is
  Port (clk : in std_logic;
  output : out std_logic_vector(15 downto 0) :="0000000000000000");
  -- out_vector represents re1,re2,we1,we2,weR,weMAC,reMAC
end Multiplier;

architecture Behavioral of Multiplier is

component FSM
  Port (clk : in std_logic;
  cntrl : in std_logic;
  out_vector : out std_logic_vector(6 downto 0);
  addr1 : out std_logic_vector(13 downto 0) := "00000000000000";
  addr2 : out std_logic_vector(13 downto 0) := "00000000000000";
  addrRAM : out std_logic_vector(13 downto 0) := "00000000000000";
  cntrl1 : out std_logic);
end component;

component MAC 
  Port (reMAC : in std_logic;
  weMAC : in std_logic;
  din1 : in std_logic_vector(7 downto 0);
  din2 : in std_logic_vector(7 downto 0);
  clk : in std_logic;
cntrl : in std_logic;
dout : out std_logic_vector(15 downto 0));
end component;

component Register8
  Port (din : in std_logic_vector(7 downto 0);
  clk : in std_logic;
  we : in std_logic;
  re : in std_logic;
  dout : out std_logic_vector(7 downto 0) );
end component;

component dist_mem_gen_0
    Port(a : in std_logic_vector(13 downto 0);
    clk : in std_logic;
    spo : out std_logic_vector(7 downto 0));
end component;

component dist_mem_gen_1
    Port(a : std_logic_vector(13 downto 0);
    clk : in std_logic;
    d : in std_logic_vector(15 downto 0);
    we : in std_logic;
    spo : out std_logic_vector(15 downto 0));
end component;

signal out_vector : std_logic_vector(6 downto 0);
signal re1 : std_logic;
signal re2 : std_logic;
signal we1 : std_logic;
signal we2 : std_logic;
signal weR : std_logic;
signal weMAC : std_logic;
signal reMAC : std_logic;
signal cntrl : std_logic;
signal cntrl1 :std_logic;
signal dout : std_logic_vector(15 downto 0);
signal din1 : std_logic_vector(7 downto 0);
signal din2 : std_logic_vector(7 downto 0);
signal addr1 : std_logic_vector(13 downto 0);
signal addr2 : std_logic_vector(13 downto 0);
signal addrRAM : std_logic_vector(13 downto 0);

begin
mainfsm : FSM port map(clk => clk,cntrl => cntrl,out_vector => out_vector,addr1 => addr1,addr2 => addr2,cntrl1 => cntrl1, addrRAM => addrRAM);
mainMAC : MAC port map(reMAC => reMAC,weMAC => weMAC,din1 => din1,din2 => din2,clk => clk,cntrl => cntrl1,dout => dout);
Reg1 : Register8 port map(din => din1,clk => clk,we => we1,re => re1,dout => din1);
Reg2 : Register8 port map(din => din2,clk => clk,we => we2,re => re1,dout => din2);
ROM1 : dist_mem_gen_0 port map(a => addr1, spo => din1, clk=>clk);
ROM2 : dist_mem_gen_0 port map(a => addr2, spo => din2, clk=>clk);
RAM : dist_mem_gen_1 port map(a => addrRAM,d => dout, clk => clk, we => weR);
re1 <= out_vector(6);
re2 <= out_vector(5);
we1 <= out_vector(4);
we2 <= out_vector(3);
weR <= out_vector(2);
weMAC <= out_vector(1);
reMAC <= out_vector(0);
cntrl <= cntrl1;
output <= dout;
end Behavioral;