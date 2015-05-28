function [layer] = pb_read_Layer(buffer, buffer_start, buffer_end)
%pb_read_Layer Reads the protobuf message Layer.
%   function [layer] = pb_read_Layer(buffer, buffer_start, buffer_end)
%
%   INPUTS:
%     buffer       : a buffer of uint8's to parse
%     buffer_start : optional starting index to consider of the buffer
%                    defaults to 1
%     buffer_end   : optional ending index to consider of the buffer
%                    defaults to length(buffer)
%
%   MEMBERS:
%     numNodes       : optional int32, defaults to int32(0).
%     isHidden       : optional uint32, defaults to uint32(0).
%
%   See also pb_read_Experiment.
  
  if (nargin < 1)
    buffer = uint8([]);
  end
  if (nargin < 2)
    buffer_start = 1;
  end
  if (nargin < 3)
    buffer_end = length(buffer);
  end
  
  descriptor = pb_descriptor_Layer();
  layer = pblib_generic_parse_from_string(buffer, descriptor, buffer_start, buffer_end);
  layer.descriptor_function = @pb_descriptor_Layer;
