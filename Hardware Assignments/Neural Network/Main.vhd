----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 10/17/2022 03:48:16 PM
-- Design Name: 
-- Module Name: Main - Behavioral
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

entity Main is
  Port (clk : in std_logic;
 an0 : in std_logic_vector(3 downto 0);
 an1 : in std_logic_vector(3 downto 0);
 an2 : in std_logic_vector(3 downto 0);
 an3 : in std_logic_vector(3 downto 0);
 seg : out std_logic_vector(6 downto 0);
 an : out std_logic_vector(3 downto 0);
 led : out std_logic_vector(15 downto 0));
  -- out_vector represents re1,re2,we1,we2,weR,weMAC,reMAC
end Main;

architecture Behavioral of Main is

component FSM
Port (clk : in std_logic;
out_vector : out std_logic_vector(6 downto 0);
addr1 : out std_logic_vector(15 downto 0) := "0000000000000000";
addr2 : out std_logic_vector(15 downto 0) := "0000000000000000";
addrRAM : out std_logic_vector(13 downto 0) := "00000000000000";
cntrl : out std_logic := '0';
outfsm : out std_logic_vector(15 downto 0);
data : in std_logic_vector(15 downto 0));
-- out_vector represents re1,re2,we1,we2,weR,weMAC,reMAC
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

component Register16
  Port (din : in std_logic_vector(15 downto 0);
  clk : in std_logic;
  we : in std_logic;
  re : in std_logic;
  dout : out std_logic_vector(15 downto 0) );
end component;

component Register8
  Port (din : in std_logic_vector(7 downto 0);
  clk : in std_logic;
  we : in std_logic;
  re : in std_logic;
  dout : out std_logic_vector(7 downto 0) );
end component;

component mem1
    Port(a : in std_logic_vector(9 downto 0);
    clk : in std_logic;
    spo : out std_logic_vector(15 downto 0));
end component;

component mem2
    Port(a : in std_logic_vector(15 downto 0);
    clk : in std_logic;
    spo : out std_logic_vector(7 downto 0));
end component;

component mem3
    Port(a : std_logic_vector(6 downto 0);
    clk : in std_logic;
    d : in std_logic_vector(15 downto 0);
    we : in std_logic;
    spo : out std_logic_vector(15 downto 0));
end component;

component mem4
    Port(a : std_logic_vector(3 downto 0);
    clk : in std_logic;
    d : in std_logic_vector(15 downto 0);
    we : in std_logic;
    spo : out std_logic_vector(15 downto 0));
end component;

--component Display
--Port (an0 : in std_logic_vector(3 downto 0);
--an1 : in std_logic_vector(3 downto 0);
--an2 : in std_logic_vector(3 downto 0);
--an3 : in std_logic_vector(3 downto 0);
--clk : in std_logic;
--seg : out std_logic_vector(6 downto 0);
--an : out std_logic_vector(3 downto 0);
--led : out std_logic_vector(15 downto 0));
--end component;

signal out_vector : std_logic_vector(6 downto 0);
signal outfsm : std_logic_vector(15 downto 0);
signal cntrl : std_logic;
signal dout : std_logic_vector(15 downto 0);
signal din1 : std_logic_vector(15 downto 0);
signal din2 : std_logic_vector(7 downto 0);
signal addr1 : std_logic_vector(15 downto 0);
signal addr2 : std_logic_vector(15 downto 0);
signal addrRAM : std_logic_vector(15 downto 0);
signal dtemp1 : std_logic_vector(15 downto 0);
signal dtemp2 : std_logic_vector(7 downto 0);
signal outptram1 : std_logic_vector(15 downto 0);
signal outptram2 : std_logic_vector(15 downto 0);
signal doutram1 : std_logic_vector(15 downto 0);
signal doutram2 : std_logic_vector(15 downto 0);
signal addrRAM1 : std_logic_vector(6 downto 0);
signal addrRAM2 : std_logic_vector(3 downto 0);
signal weRAM1 : std_logic;
signal weRAM2 : std_logic;
signal addrrom1 : std_logic_vector(9 downto 0);
signal addrrom2 : std_logic_vector(15 downto 0);
begin
dtemp1 <= (din1 and (not outfsm)) or (outptram1 and outfsm);
dtemp2 <= din2;
addrRAM1 <= (addrRAM(6 downto 0) and (not outfsm(6 downto 0))) or (addr1(6 downto 0) and outfsm(6 downto 0));
addrRAM2 <= addrRAM(3 downto 0) and (outfsm(3 downto 0)); 
doutram1 <= dout and (not outfsm);
doutram2 <= dout and outfsm;
weRAM1 <= out_vector(2) and (not outfsm(0));
weRAM2 <= out_vector(2) and outfsm(0);
mainfsm : FSM port map(clk => clk,cntrl => cntrl,out_vector => out_vector,addr1 => addr1,addr2 => addr2, addrRAM => addrRAM,outfsm => outfsm,data => outptram2);
mainMAC : MAC port map(reMAC => out_vector(0),weMAC => out_vector(1),din1 => dtemp1,din2 => dtemp2,clk => clk,cntrl => cntrl,dout => dout);
Reg1 : Register16 port map(din => din1,clk => clk,we => out_vector(4),re => out_vector(6),dout => dtemp1);
Reg2 : Register8 port map(din => din2,clk => clk,we => out_vector(3),re => out_vector(5),dout => dtemp2);
ROM1 : mem1 port map(a => (addr1(9 downto 0) and (not outfsm(9 downto 0))) , spo => din1, clk=>clk);
ROM2 : mem2 port map(a => addr2, spo => din2, clk=>clk);
RAM1 : mem3 port map(a => addrRAM1,d => doutram1, clk => clk, we => weRAM1,spo => outptram1);
RAM2 : mem4 port map(a => addrRAM2,d => doutram2, clk => clk, we => weRAM2,spo => outptram2);
-- process(clk)
-- begin
--   if(outfsm = '0') then
--     addrrom1 <= addr1(9 downto 0);
--     addrrom2 <= addr2;
--     dtemp1 <= din1;
--     dtemp2 <= din2;
--     addrRAM1 <= addrRAM(6 downto 0);
--     addrRAM2 <= "0000";
--     doutram1 <= dout;
--     doutram2 <= "0000000000000000";
--     weRAM1 <= out_vector(2); 
--     weRAM2 <= '0';
--   else 
--     addrrom1 <= "0000000000";
--     addrrom2 <= addr2;
--     dtemp1 <= outptram1; 
--     dtemp2 <= din2;
--     addrRAM1 <= addr1(6 downto 0);
--     addrRAM2 <= addrRAM(3 downto 0);
--     doutram1 <= "0000000000000000";
--     doutram2 <= dout;
--     weRAM1 <= '0';
--     weRAM2 <= out_vector(2);
--   end if;
--   end process;
end Behavioral;