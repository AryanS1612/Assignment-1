// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.1 (lin64) Build 3526262 Mon Apr 18 15:47:01 MDT 2022
// Date        : Mon Nov  7 13:29:19 2022
// Host        : dhd running 64-bit Ubuntu 20.04.3 LTS
// Command     : write_verilog -force -mode synth_stub -rename_top dist_mem_gen_1 -prefix
//               dist_mem_gen_1_ dist_mem_gen_1_stub.v
// Design      : dist_mem_gen_1
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "dist_mem_gen_v8_0_13,Vivado 2022.1" *)
module dist_mem_gen_1(a, d, clk, we, spo)
/* synthesis syn_black_box black_box_pad_pin="a[13:0],d[15:0],clk,we,spo[15:0]" */;
  input [13:0]a;
  input [15:0]d;
  input clk;
  input we;
  output [15:0]spo;
endmodule
