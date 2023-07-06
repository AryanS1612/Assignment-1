// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.1 (lin64) Build 3526262 Mon Apr 18 15:47:01 MDT 2022
// Date        : Tue Nov  1 02:23:52 2022
// Host        : dhd running 64-bit Ubuntu 20.04.3 LTS
// Command     : write_verilog -force -mode synth_stub {/home/btech/cs1210549/Assignment 3/Assignment
//               3.gen/sources_1/ip/dist_mem_gen_0/dist_mem_gen_0_stub.v}
// Design      : dist_mem_gen_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "dist_mem_gen_v8_0_13,Vivado 2022.1" *)
module dist_mem_gen_0(a, spo)
/* synthesis syn_black_box black_box_pad_pin="a[13:0],spo[7:0]" */;
  input [13:0]a;
  output [7:0]spo;
endmodule
