# This program generates required data and put the data into required form to apply machine/deep learning
# in a step by step way.
# Set the parameters first before running it.
# Steps are in general independent from another steps except dependence on data consumed by some steps
# are generated by previous steps.

# -- imports --
import cs_designite_runner
import cs_code_split_runner
import cs_learning_data_generator
import tokenizer_runner
import java_designite_runner
import java_codeSplit_runner
import java_learning_data_generator
# --

# -- Parameters --
DATA_BASE_PATH = r'D:\research\smellDetectionML\data'
CS_REPO_SOURCE_FOLDER = DATA_BASE_PATH + r'\all_cs_repos'
BATCH_FILES_FOLDER = DATA_BASE_PATH + r'\BatchFiles'
CS_SMELLS_RESULTS_FOLDER = DATA_BASE_PATH + r'\designite_out'
CS_DESIGNITE_CONSOLE_PATH = "C:\\Program Files (x86)\\Designite\\DesigniteConsole.exe"

CS_CODE_SPLIT_OUT_FOLDER_CLASS = DATA_BASE_PATH + r'\codesplit_out_class'
CS_CODE_SPLIT_OUT_FOLDER_METHOD = DATA_BASE_PATH + r'\codesplit_out_method'
CS_CODE_SPLIT_MODE_CLASS = "-c"
CS_CODE_SPLIT_MODE_METHOD = "-m"
CS_CODE_SPLIT_EXE_PATH = r'D:\Dev\codeSplit\CodeSplit\bin\Release\CodeSplit.exe'

CS_LEARNING_DATA_FOLDER_BASE = DATA_BASE_PATH + r'\training_data'
# CS_LEARNING_DATA_FOLDER_BASE = "/Users/Tushar/Documents/Research/smellDetectionML/data/smellML_Data_cs"

# TOKENIZER_EXE_PATH = "/Users/Tushar/Documents/Research/smellDetectionML/tokenizer/src/tokenizer"
TOKENIZER_EXE_PATH = r'D:\research\smellDetectionML\tokenizer\src\tokenizer.exe'
CS_TOKENIZER_OUT_PATH = DATA_BASE_PATH + r'\tokenizer_out'
# CS_TOKENIZER_OUT_PATH = "/Users/Tushar/Documents/Research/smellDetectionML/data/tokenizer_out_cs"

JAVA_REPO_SOURCE_FOLDER = DATA_BASE_PATH + r'\all_java_repos'
JAVA_SMELLS_RESULTS_FOLDER = DATA_BASE_PATH + r'\designite_out_java'
DESIGNITE_JAVA_JAR_PATH = r'D:\research\smellDetectionML\dj\DesigniteJava.jar'

JAVA_CODE_SPLIT_OUT_FOLDER_CLASS = DATA_BASE_PATH + r'\codesplit_java_class'
JAVA_CODE_SPLIT_OUT_FOLDER_METHOD = DATA_BASE_PATH + r'\codesplit_java_method'
JAVA_CODE_SPLIT_MODE_CLASS = "class"
JAVA_CODE_SPLIT_MODE_METHOD = "method"
JAVA_CODE_SPLIT_EXE_PATH = r'D:\research\smellDetectionML\CodeSplitJava\target\CodeSplitJava.jar'

JAVA_LEARNING_DATA_FOLDER_BASE = DATA_BASE_PATH + r'\smellML_data_java'

JAVA_TOKENIZER_OUT_PATH = DATA_BASE_PATH + r'\tokenizer_out_java'
# --

if __name__ == "__main__":
    # 1. Run Designite to analyze C# repositories
    # This step requires that you have downloaded C# repositories to analyze and have installed
    # Designite on your machine. Designite can be downloaded from its website (http://www.designite-tools.com).
    # cs_designite_runner.analyze_repositories(CS_REPO_SOURCE_FOLDER, BATCH_FILES_FOLDER, CS_SMELLS_RESULTS_FOLDER,
    #                                         CS_DESIGNITE_CONSOLE_PATH)

    # 2. Run codeSplit for all C# repositories
    # 2.1 Run codeSplit to generate class code fragments (each code fragment will contain a class definition)
    # cs_code_split_runner.cs_code_split(CS_REPO_SOURCE_FOLDER, CS_CODE_SPLIT_OUT_FOLDER_CLASS, CS_CODE_SPLIT_MODE_CLASS,
    #                                  CS_CODE_SPLIT_EXE_PATH)

    # 2.2 Run codeSplit to generate method code fragments (each code fragment will contain a method definition)
    # cs_code_split_runner.cs_code_split(CS_REPO_SOURCE_FOLDER, CS_CODE_SPLIT_OUT_FOLDER_METHOD, CS_CODE_SPLIT_MODE_METHOD,
    #                                  CS_CODE_SPLIT_EXE_PATH)

    # 3. Run learning data generator that will classify code fragments into either positive or negative cases
    # based on occurrence of smell in that fragment
    # cs_learning_data_generator.generate_data(CS_SMELLS_RESULTS_FOLDER, CS_CODE_SPLIT_OUT_FOLDER_CLASS,
    #                                        CS_CODE_SPLIT_OUT_FOLDER_METHOD, CS_LEARNING_DATA_FOLDER_BASE)

    # 4. Run tokenizer to convert code fragments into vectors/matrices of numbers that can be fed to neural network.
    # tokenizer_runner.tokenize("CSharp", CS_LEARNING_DATA_FOLDER_BASE, CS_TOKENIZER_OUT_PATH, TOKENIZER_EXE_PATH)

    # 5-8. We repeat the step 1 to 4 for Java repositories
    # 5. Run DesigniteJava to analyze Java repositories
    # java_designite_runner.analyze_repositories(JAVA_REPO_SOURCE_FOLDER, JAVA_SMELLS_RESULTS_FOLDER, DESIGNITE_JAVA_JAR_PATH)

    # 6. Run CodeSplit for all Java repositories
    # 6.1 Run codeSplit to generate class code fragments
    # java_codeSplit_runner.java_code_split(JAVA_REPO_SOURCE_FOLDER, JAVA_CODE_SPLIT_MODE_CLASS,
    #                                       JAVA_CODE_SPLIT_OUT_FOLDER_CLASS, JAVA_CODE_SPLIT_EXE_PATH)

    # 6.2 Run codeSplit to generate method code fragments
    # java_codeSplit_runner.java_code_split(JAVA_REPO_SOURCE_FOLDER, JAVA_CODE_SPLIT_MODE_METHOD,
    #                                       JAVA_CODE_SPLIT_OUT_FOLDER_METHOD, JAVA_CODE_SPLIT_EXE_PATH)

    # 7. Run learning data generator that will classify java code fragments into either positive or negative cases
    #     # based on occurrence of smell in that fragment
    # java_learning_data_generator.generate_data(JAVA_SMELLS_RESULTS_FOLDER, JAVA_CODE_SPLIT_OUT_FOLDER_CLASS,
    #                                            JAVA_CODE_SPLIT_OUT_FOLDER_METHOD, JAVA_LEARNING_DATA_FOLDER_BASE)

    # 8. Run tokenizer to convert code fragments into vectors/matrices of numbers that can be fed to neural network.
    tokenizer_runner.tokenize("Java", JAVA_LEARNING_DATA_FOLDER_BASE, JAVA_TOKENIZER_OUT_PATH, TOKENIZER_EXE_PATH)