function [descriptor] = pb_descriptor_Layer()
%pb_descriptor_Layer Returns the descriptor for message Layer.
%   function [descriptor] = pb_descriptor_Layer()
%
%   See also pb_read_Layer
  
  descriptor = struct( ...
    'name', 'Layer', ...
    'full_name', 'Layer', ...
    'filename', 'dbm.proto', ...
    'containing_type', '', ...
    'fields', [ ...
      struct( ...
        'name', 'numNodes', ...
        'full_name', 'Layer.numNodes', ...
        'index', 1, ...
        'number', uint32(1), ...
        'type', uint32(5), ...
        'matlab_type', uint32(1), ...
        'wire_type', uint32(0), ...
        'label', uint32(1), ...
        'default_value', int32(0), ...
        'read_function', @(x) pblib_helpers_first(typecast(x, 'int32')), ...
        'write_function', @(x) typecast(int32(x), 'uint32'), ...
        'options', struct('packed', false) ...
      ), ...
      struct( ...
        'name', 'isHidden', ...
        'full_name', 'Layer.isHidden', ...
        'index', 2, ...
        'number', uint32(2), ...
        'type', uint32(8), ...
        'matlab_type', uint32(3), ...
        'wire_type', uint32(0), ...
        'label', uint32(1), ...
        'default_value', uint32(0), ...
        'read_function', @(x) pblib_helpers_first(typecast(x, 'uint32')), ...
        'write_function', @(x) typecast(uint32(x), 'uint32'), ...
        'options', struct('packed', false) ...
      ) ...
    ], ...
    'extensions', [ ... % Not Implemented
    ], ...
    'nested_types', [ ... % Not implemented
    ], ...
    'enum_types', [ ... % Not Implemented
    ], ...
    'options', [ ... % Not Implemented
    ] ...
  );
  
  descriptor.field_indeces_by_number = java.util.HashMap;
  put(descriptor.field_indeces_by_number, uint32(1), 1);
  put(descriptor.field_indeces_by_number, uint32(2), 2);
  
