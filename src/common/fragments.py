from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import pandas as pd
import streamlit as st

from src.common.utils import get_bar_plot


def _parse_config_field(
    text_input: str,
    csv_file: Optional[Path] = None,
    column: Optional[str] = None,
) -> Optional[set]:
    """
    Parses text input and csv file. If both text and file are passed, the results of their parsing are merged.
    """

    words = set()

    if text_input != '':
        words.update({word.strip() for word in text_input.split(',') if word})

    if csv_file is not None:
        df = pd.read_csv(csv_file, keep_default_na=False)

        if column is None:
            st.error('Failed to read data from file. The column name was not passed.')
        elif column not in df.columns:
            st.error(f'Failed to read data from file. The column named "{column}" is not in the given table.')
        else:
            words.update(df[column].to_list())

    if not words:
        return None

    return words


def _show_config_field(
    *,
    text_input_label: str,
    text_input_help: Optional[str],
    file_uploader_label: str,
    file_uploader_help: Optional[str],
    key: str,
) -> Tuple[Optional[str], Optional[Path]]:
    left_column, right_column = st.columns(2)

    with left_column:
        text = st.text_input(label=text_input_label, help=text_input_help, key=f'{key}_text_input')

    with right_column:
        file = st.file_uploader(
            label=file_uploader_label,
            help=file_uploader_help,
            type=['csv'],
            key=f'{key}_file_uploader',
        )

    return text, file


def _show_bar_plot_config(key: str) -> Dict[str, Any]:
    with st.expander('Config'):
        left_column, _ = st.columns(2)
        with left_column:
            bars_count = st.number_input(
                'bars_count:',
                value=50,
                key=f'{key}_bars_count',
                help='Number of bars to show from start in sorted by count order.',
            )

        bars_ignore_text_input, bars_ignore_csv_file = _show_config_field(
            text_input_label='bars_ignore:',
            text_input_help=(
                'Ignore bars with names start with one from this set. Names should be separated by a comma.'
            ),
            file_uploader_label='bars_ignore:',
            file_uploader_help=(
                'Ignore bars with names start with one from this set. A CSV file which contains column `package_name`.'
            ),
            key=f'{key}_bars_ignore',
        )

        bars_ignore = _parse_config_field(bars_ignore_text_input, bars_ignore_csv_file, 'package_name')

        bars_select_text_input, bars_select_csv_file = _show_config_field(
            text_input_label='bars_select:',
            text_input_help=(
                'Select bars with names start with one from this set. Names should be separated by a comma.'
            ),
            file_uploader_label='bars_select:',
            file_uploader_help=(
                'Select bars with names start with one from this set. A CSV file which contains column `package_name`.'
            ),
            key=f'{key}_bars_select',
        )

        bars_select = _parse_config_field(bars_select_text_input, bars_select_csv_file, 'package_name')

        return {
            'bars_count': int(bars_count),
            'bars_ignore': bars_ignore,
            'bars_select': bars_select,
        }


def show_bar_plot_with_config(
    *,
    header: str,
    description: Optional[str] = None,
    df: pd.DataFrame,
    x_axis: str,
    y_axis: Union[str, List[str]],
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    sort_by: Optional[Union[str, List[str]]] = None,
    key: str,
):
    st.header(header)

    if description is not None:
        st.markdown(description)

    config = _show_bar_plot_config(key=key)
    fig = get_bar_plot(df, x=x_axis, y=y_axis, x_title=x_title, y_title=y_title, sort_by=sort_by, **config)
    st.plotly_chart(fig, use_container_width=True)
