{
    "targets": [{
        "target_name": "neon",
        "sources": [ "src/neon.cc" ],
        "include_dirs": [ "<!(node -e \"require('nan')\")" ],
        'configurations': {
            'Release': {
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'WholeProgramOptimization': 'false',
                        'RuntimeLibrary': 3
                    },
                    'VCLinkerTool': {
                        'LinkTimeCodeGeneration': 0
                    }
                }
            },
            'Debug': {
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'RuntimeLibrary': '0',
                        'UndefinePreprocessorDefinitions': ['DEBUG', '_DEBUG'],
                        'PreprocessorDefinitions': ['NDEBUG']
                    }
                }
            }
        }
    }]
}
