function [job] = pb_read_Job(buffer, buffer_start, buffer_end)
%pb_read_Job Reads the protobuf message Job.
%   function [job] = pb_read_Job(buffer, buffer_start, buffer_end)
%
%   INPUTS:
%     buffer       : a buffer of uint8's to parse
%     buffer_start : optional starting index to consider of the buffer
%                    defaults to 1
%     buffer_end   : optional ending index to consider of the buffer
%                    defaults to length(buffer)
%
%   MEMBERS:
%     expid          : required string, defaults to ''.
%     description    : required string, defaults to ''.
%     binary         : required string, defaults to ''.
%     args           : optional string, defaults to ''.
  
  if (nargin < 1)
    buffer = uint8([]);
  end
  if (nargin < 2)
    buffer_start = 1;
  end
  if (nargin < 3)
    buffer_end = length(buffer);
  end
  
  descriptor = pb_descriptor_Job();
  job = pblib_generic_parse_from_string(buffer, descriptor, buffer_start, buffer_end);
  job.descriptor_function = @pb_descriptor_Job;
