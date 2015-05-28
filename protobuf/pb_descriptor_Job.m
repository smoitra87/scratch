function [descriptor] = pb_descriptor_Job()
%pb_descriptor_Job Returns the descriptor for message Job.
%   function [descriptor] = pb_descriptor_Job()
%
%   See also pb_read_Job
  
  descriptor = struct( ...
    'name', 'Job', ...
    'full_name', 'Job', ...
    'filename', 'job.proto', ...
    'containing_type', '', ...
    'fields', [ ...
      struct( ...
        'name', 'expid', ...
        'full_name', 'Job.expid', ...
        'index', 1, ...
        'number', uint32(1), ...
        'type', uint32(9), ...
        'matlab_type', uint32(7), ...
        'wire_type', uint32(2), ...
        'label', uint32(2), ...
        'default_value', '', ...
        'read_function', @(x) char(x{1}(x{2} : x{3})), ...
        'write_function', @uint8, ...
        'options', struct('packed', false) ...
      ), ...
      struct( ...
        'name', 'description', ...
        'full_name', 'Job.description', ...
        'index', 2, ...
        'number', uint32(2), ...
        'type', uint32(9), ...
        'matlab_type', uint32(7), ...
        'wire_type', uint32(2), ...
        'label', uint32(2), ...
        'default_value', '', ...
        'read_function', @(x) char(x{1}(x{2} : x{3})), ...
        'write_function', @uint8, ...
        'options', struct('packed', false) ...
      ), ...
      struct( ...
        'name', 'binary', ...
        'full_name', 'Job.binary', ...
        'index', 3, ...
        'number', uint32(3), ...
        'type', uint32(9), ...
        'matlab_type', uint32(7), ...
        'wire_type', uint32(2), ...
        'label', uint32(2), ...
        'default_value', '', ...
        'read_function', @(x) char(x{1}(x{2} : x{3})), ...
        'write_function', @uint8, ...
        'options', struct('packed', false) ...
      ), ...
      struct( ...
        'name', 'args', ...
        'full_name', 'Job.args', ...
        'index', 4, ...
        'number', uint32(4), ...
        'type', uint32(9), ...
        'matlab_type', uint32(7), ...
        'wire_type', uint32(2), ...
        'label', uint32(1), ...
        'default_value', '', ...
        'read_function', @(x) char(x{1}(x{2} : x{3})), ...
        'write_function', @uint8, ...
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
  put(descriptor.field_indeces_by_number, uint32(3), 3);
  put(descriptor.field_indeces_by_number, uint32(4), 4);
  
