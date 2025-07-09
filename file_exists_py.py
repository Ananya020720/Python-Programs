{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnu5JDC6e774KpgSQlkpuX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ananya020720/Python-Programs/blob/main/file_exists_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZmUtkltfvEaP",
        "outputId": "da8ab05c-bb8f-4a33-a21f-50e2ad498486"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "File 'example.txt' does not exist.\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "\n",
        "file_path = 'example.txt'\n",
        "\n",
        "if os.path.exists(file_path):\n",
        "    print(f\"File '{file_path}' exists. Its contents are:\\n\")\n",
        "    with open(file_path, 'r') as file:\n",
        "        content = file.read()\n",
        "        print(content)\n",
        "else:\n",
        "    print(f\"File '{file_path}' does not exist.\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "FC5PX3cL0749"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}